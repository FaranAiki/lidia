import pandas as pd
import os

filepath = 'dataset/RLS_province.csv'
df = pd.read_csv(filepath)

# Pivot the table: index is province name, columns are years, values are RLS
df_pivot = df.pivot(index='nama_provinsi', columns='tahun', values='rata_rata_lama_sekolah')

# Sort years just in case
years = sorted(df_pivot.columns)

# Rename columns to "rata_rata_lama_sekolah (YEAR)" as requested
df_pivot.columns = [f"rata_rata_lama_sekolah ({year})" for year in years]

# Reset index to bring "nama_provinsi" back as a column
df_pivot.reset_index(inplace=True)

# Rename "nama_provinsi" to match the style of other datasets if needed? 
# The user said "sesuai dengan dataset yang lain".
# PPK.csv uses "Provinsi/Kabupaten/Kota/Indonesia"
# Let's keep "nama_provinsi" or use a more generic "Provinsi"
df_pivot.rename(columns={'nama_provinsi': 'Provinsi'}, inplace=True)

output_path = 'dataset/RLS_province_normalized.csv'
df_pivot.to_csv(output_path, index=False)

print(f"Successfully normalized RLS data to {output_path}")
print(df_pivot.head())
