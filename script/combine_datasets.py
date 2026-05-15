import pandas as pd
import os
import re

def normalize_name(name):
    if not isinstance(name, str):
        return name
    name = name.strip().upper()
    # Normalize common variations
    mappings = {
        'DKI JAKARTA': 'DAERAH KHUSUS JAKARTA',
        'JAKARTA': 'DAERAH KHUSUS JAKARTA',
        'DI YOGYAKARTA': 'DAERAH ISTIMEWA YOGYAKARTA',
        'D I YOGYAKARTA': 'DAERAH ISTIMEWA YOGYAKARTA',
        'YOGYAKARTA': 'DAERAH ISTIMEWA YOGYAKARTA',
        'KEP. RIAU': 'KEPULAUAN RIAU',
        'KEP. BANGKA BELITUNG': 'KEPULAUAN BANGKA BELITUNG',
        'KEP BANGKA BELITUNG': 'KEPULAUAN BANGKA BELITUNG',
    }
    return mappings.get(name, name)

# Load official province list for final names
with open('dataset/daftar_provinsi.txt', 'r') as f:
    official_provinces = [line.strip() for line in f if line.strip()]
norm_to_official = {normalize_name(p): p for p in official_provinces}

files = [
    'dataset/APM_final.csv',
    'dataset/IPM_final.csv',
    'dataset/PPK_final.csv',
    'dataset/PSN_final.csv',
    'dataset/RLS_final.csv'
]

combined_df = None

for file in files:
    print(f"Processing {file}...")
    df = pd.read_csv(file)
    
    # Normalize names to official ones
    df['Provinsi'] = df['Provinsi'].apply(normalize_name).map(norm_to_official)
    
    # Sort by official name
    df = df.sort_values(by='Provinsi')
    
    # Save sorted version back to file
    df.to_csv(file, index=False)
    
    if combined_df is None:
        combined_df = df
    else:
        combined_df = pd.merge(combined_df, df, on='Provinsi', how='outer')

# Final sort
combined_df = combined_df.sort_values(by='Provinsi')

# Save combined dataset
output_path = 'dataset/combined_dataset.csv'
combined_df.to_csv(output_path, index=False)

print(f"Successfully combined all datasets into {output_path}")
print(f"Total rows: {len(combined_df)}")
print(f"Total columns: {len(combined_df.columns)}")
print(combined_df[['Provinsi']].head(10))
