import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data, skipping the first line header
filepath = 'dataset/PSN_province.csv'
df = pd.read_csv(filepath, skiprows=1)

# Clean numeric values: convert "13,4" to 13.4
year_cols = ['2020', '2021', '2022', '2023']
for col in year_cols:
    if df[col].dtype == object:
        df[col] = df[col].str.replace(',', '.').astype(float)

years = [int(y) for y in year_cols]
last_year = max(years)

# 1. Calculate average slope
slopes = []
for idx, row in df.iterrows():
    y_values = row[year_cols].values.astype(float)
    mask = ~np.isnan(y_values)
    if np.sum(mask) >= 2:
        x = np.array(years)[mask].reshape(-1, 1)
        y = y_values[mask]
        model = LinearRegression().fit(x, y)
        slopes.append(model.coef_[0])

avg_slope = np.mean(slopes) if slopes else 0
print(f"PSN average annual growth rate (slope): {avg_slope:.4f}")

# 2. Back-extrapolate
def fill_missing(row):
    val_last = row[str(last_year)]
    if pd.isna(val_last):
        available_years = [int(y) for y in year_cols if not pd.isna(row[y])]
        if not available_years:
            return row
        ref_year = max(available_years)
        val_last = row[str(ref_year)]
    else:
        ref_year = last_year
    
    for year in years:
        col = str(year)
        if pd.isna(row[col]):
            row[col] = round(val_last - (ref_year - year) * avg_slope, 2)
            row[col] = max(0, row[col]) # Stunting can't be negative
    return row

df_filled = df.apply(fill_missing, axis=1)

# Rename columns
df_filled.columns = ['Provinsi'] + [f"PSN ({year})" for year in years]

# Save
output_path = 'dataset/PSN_final.csv'
df_filled.to_csv(output_path, index=False)

print(f"Successfully processed PSN data to {output_path}")
print(df_filled.head())
