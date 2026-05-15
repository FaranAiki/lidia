import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data, skipping the messy first two header rows
filepath = 'dataset/PPK_province.csv'
# The 3rd row (index 2) contains the years
df = pd.read_csv(filepath, skiprows=2)

# Rename the first column to 'Provinsi'
df.rename(columns={df.columns[0]: 'Provinsi'}, inplace=True)

# Replace '-' with NaN and convert to numeric
year_cols = [col for col in df.columns if col.isdigit()]
for col in year_cols:
    df[col] = pd.to_numeric(df[col].replace('-', np.nan), errors='coerce')

years = [int(y) for y in year_cols]
last_year = max(years)

# 1. Calculate average slope (growth rate) from provinces with complete data
slopes = []
for idx, row in df.iterrows():
    y_values = row[year_cols].values.astype(float)
    mask = ~np.isnan(y_values)
    if np.sum(mask) > 3: # Enough data points for a trend
        x = np.array(years)[mask].reshape(-1, 1)
        y = y_values[mask]
        model = LinearRegression().fit(x, y)
        slopes.append(model.coef_[0])

avg_slope = np.mean(slopes) if slopes else 0
print(f"PPK average annual growth rate (slope): {avg_slope:.4f}")

# 2. Back-extrapolate missing values
def fill_missing(row):
    # Use the 2025 value (last_year) as reference
    val_last = row[str(last_year)]
    if pd.isna(val_last):
        # Try to find the latest available year if 2025 is missing
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
            # Value(Year) = Value(Ref) - (Ref - Year) * avg_slope
            row[col] = round(val_last - (ref_year - year) * avg_slope, 0)
    return row

df_filled = df.apply(fill_missing, axis=1)

# Rename columns to follow the requested style: "PPK (Year)"
# Or maybe just keep years if preferred, but for consistency with APM/RLS:
df_filled.columns = ['Provinsi'] + [f"PPK ({year})" for year in years]

# Save to PPK_final.csv
output_path = 'dataset/PPK_final.csv'
df_filled.to_csv(output_path, index=False)

print(f"Successfully processed PPK data to {output_path}")
print(df_filled[df_filled['Provinsi'].str.contains('PAPUA')].head())
