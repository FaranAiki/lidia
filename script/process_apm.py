import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the data
filepath = 'dataset/APM_province.csv'
df = pd.read_csv(filepath)

# Replace '-' with NaN and convert columns to numeric
cols_to_fix = ['SD/sederajat', 'SMP/sederajat', 'SM/sederajat']
for col in cols_to_fix:
    df[col] = pd.to_numeric(df[col].replace('-', np.nan), errors='coerce')

# Pivot the data
# We want: Provinsi as index, and (Indicator, Tahun) as multi-columns
df_pivot = df.pivot(index='Provinsi', columns='Tahun', values=cols_to_fix)

# Flatten columns: "SD/sederajat (2003)", "SMP/sederajat (2003)", etc.
# The user wants "rata_rata_lama sekolah (2010)" style, so let's follow that.
new_columns = []
for indicator, year in df_pivot.columns:
    new_columns.append(f"{indicator} ({year})")
df_pivot.columns = new_columns
df_pivot.reset_index(inplace=True)

# Analysis and Filling missing values
# Indicators to process
indicators = ['SD/sederajat', 'SMP/sederajat', 'SM/sederajat']
years = sorted(df['Tahun'].unique())
last_year = max(years)

# For each indicator, calculate average slope and back-extrapolate
for indicator in indicators:
    indicator_cols = [f"{indicator} ({year})" for year in years]
    
    # 1. Calculate average slope for this indicator
    slopes = []
    for idx, row in df_pivot.iterrows():
        y_values = row[indicator_cols].values.astype(float)
        mask = ~np.isnan(y_values)
        if np.sum(mask) > 5:
            x = np.array(years)[mask].reshape(-1, 1)
            y = y_values[mask]
            model = LinearRegression().fit(x, y)
            slopes.append(model.coef_[0])
    
    avg_slope = np.mean(slopes) if slopes else 0
    print(f"Indicator '{indicator}' average slope: {avg_slope:.4f}")

    # 2. Back-extrapolate missing values
    col_last = f"{indicator} ({last_year})"
    
    def fill_indicator(row):
        val_last = row[col_last]
        if pd.isna(val_last):
            # If 2025 is missing, we try to find the latest available year
            available_years = [y for y in years if not pd.isna(row[f"{indicator} ({y})"])]
            if not available_years:
                return row
            latest_y = max(available_years)
            val_last = row[f"{indicator} ({latest_y})"]
            ref_year = latest_y
        else:
            ref_year = last_year
            
        for year in years:
            col = f"{indicator} ({year})"
            if pd.isna(row[col]):
                # Value(Year) = Value(Ref) - (Ref - Year) * avg_slope
                row[col] = round(val_last - (ref_year - year) * avg_slope, 2)
                # Cap at 100% and floor at 0% for APM
                row[col] = max(0, min(100, row[col]))
        return row

    df_pivot = df_pivot.apply(fill_indicator, axis=1)

# Save the final result
output_path = 'dataset/APM_final.csv'
df_pivot.to_csv(output_path, index=False)

print(f"Successfully processed APM data to {output_path}")
print(df_pivot.head())
