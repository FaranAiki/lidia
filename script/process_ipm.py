import pandas as pd
import numpy as np

# Load the data, skipping the first 3 lines of messy headers
filepath = 'dataset/IPM_province.csv'
df = pd.read_csv(filepath, skiprows=3)

# The columns after skiprows=3 are: Location, Laki-laki (2025), Perempuan (2025)
df.columns = ['Provinsi', 'IPM Laki-laki (2025)', 'IPM Perempuan (2025)']

# Save to IPM_final.csv
output_path = 'dataset/IPM_final.csv'
df.to_csv(output_path, index=False)

print(f"Successfully processed IPM data to {output_path}")
print(df.head())
