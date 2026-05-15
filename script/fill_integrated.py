import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Load the integrated data
df = pd.read_csv('dataset/integrated.csv')

# Indicators to fill
indicators = [
    'APM_SD', 'APM_SMP', 'APM_SMA', 
    'IPM_Laki_Laki', 'IPM_Perempuan', 
    'PPK', 'PSN (Stunting)', 'RLS'
]

# Get unique provinces and years
provinces = df['Provinsi'].unique()
years = sorted(df['Tahun'].unique())

def fill_missing_for_column(df, column):
    print(f"Filling missing values for {column}...")
    
    # 1. Calculate a "Global Average Slope" for this indicator
    # This helps when a province has very few data points
    all_slopes = []
    for prov in provinces:
        prov_data = df[df['Provinsi'] == prov].dropna(subset=[column])
        if len(prov_data) >= 2:
            X = prov_data[['Tahun']].values
            y = prov_data[column].values
            model = LinearRegression().fit(X, y)
            all_slopes.append(model.coef_[0])
    
    avg_slope = np.mean(all_slopes) if all_slopes else 0
    print(f"  Average slope for {column}: {avg_slope:.4f}")
    
    # 2. Fill missing values for each province
    for prov in provinces:
        prov_mask = df['Provinsi'] == prov
        prov_data = df[prov_mask].sort_values('Tahun')
        
        # Available data for this province
        available = prov_data.dropna(subset=[column])
        
        if len(available) == 0:
            # No data at all for this province? (Shouldn't happen with our previous steps)
            continue
            
        # If we have at least one data point, we can extrapolate
        # We'll use the province's own trend if they have >= 3 points, 
        # otherwise we use the global average slope.
        if len(available) >= 3:
            X_own = available[['Tahun']].values
            y_own = available[column].values
            prov_slope = LinearRegression().fit(X_own, y_own).coef_[0]
        else:
            prov_slope = avg_slope
            
        # Anchor point (latest available)
        anchor_row = available.iloc[-1]
        anchor_year = anchor_row['Tahun']
        anchor_val = anchor_row[column]
        
        # Fill missing
        for idx, row in df[prov_mask].iterrows():
            if pd.isna(row[column]):
                target_year = row['Tahun']
                # Extrapolate: Val = Anchor + (TargetYear - AnchorYear) * Slope
                new_val = anchor_val + (target_year - anchor_year) * prov_slope
                
                # Logic constraints
                if column.startswith('APM') or column == 'PSN (Stunting)':
                    new_val = max(0, min(100, new_val))
                if column == 'RLS':
                    new_val = max(0, new_val)
                if column == 'PPK':
                    new_val = max(0, new_val)
                
                df.at[idx, column] = round(new_val, 2)

for col in indicators:
    fill_missing_for_column(df, col)

# Final save
output_path = 'dataset/integrated_filled.csv'
df.to_csv(output_path, index=False)
print(f"Successfully saved filled dataset to {output_path}")
print(df.head(10))
