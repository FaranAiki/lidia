import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the pivoted data
filepath = 'dataset/RLS_province_normalized.csv'
df = pd.read_csv(filepath)

# Identify year columns
year_cols = [col for col in df.columns if '(' in col]
years = [int(col.split('(')[1].split(')')[0]) for col in year_cols]
year_to_col = dict(zip(years, year_cols))

# 1. Calculate the average slope (growth rate) from complete datasets
slopes = []
for idx, row in df.iterrows():
    # Only use provinces that have data for most years to get a reliable growth trend
    y_values = row[year_cols].values.astype(float)
    mask = ~np.isnan(y_values)
    
    if np.sum(mask) > 5: # If we have enough data points
        x = np.array(years)[mask].reshape(-1, 1)
        y = y_values[mask]
        model = LinearRegression().fit(x, y)
        slopes.append(model.coef_[0])

avg_slope = np.mean(slopes)
print(f"Average annual growth rate (slope) calculated: {avg_slope:.4f}")

# 2. Fill missing values using the 2024 value and the average slope
# We back-extrapolate: Value(Year) = Value(2024) - (2024 - Year) * avg_slope
col_2024 = 'rata_rata_lama_sekolah (2024)'

def fill_missing(row):
    val_2024 = row[col_2024]
    if pd.isna(val_2024):
        return row # Can't do much if 2024 is also missing, but in our case it's present
    
    for year in years:
        col = year_to_col[year]
        if pd.isna(row[col]):
            # Back-extrapolate from 2024
            row[col] = round(val_2024 - (2024 - year) * avg_slope, 2)
    return row

df_filled = df.apply(fill_missing, axis=1)

# Save the result
output_path = 'dataset/RLS_province_normalized.csv' # Overwriting with filled data
df_filled.to_csv(output_path, index=False)

print(f"Filled missing values and saved to {output_path}")
# Show some of the previously empty rows (e.g., Papua Barat Daya)
print(df_filled[df_filled['Provinsi'].str.contains('PAPUA')].head(10))
