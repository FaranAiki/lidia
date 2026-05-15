import pandas as pd
import re

def normalize_name(name):
    if not isinstance(name, str):
        return name
    name = name.strip().upper()
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

# Load official province names
with open('dataset/daftar_provinsi.txt', 'r') as f:
    official_provinces = [line.strip() for line in f if line.strip()]
norm_to_official = {normalize_name(p): p for p in official_provinces}

def process_to_long(filepath, indicator_map=None):
    df = pd.read_csv(filepath)
    df['Provinsi'] = df['Provinsi'].apply(normalize_name).map(norm_to_official)
    
    # Melt the dataframe
    melted = df.melt(id_vars=['Provinsi'], var_name='Raw_Col', value_name='Value')
    
    # Extract Indicator and Year from "Indicator (Year)"
    # Example: "SD/sederajat (2003)" -> indicator="SD/sederajat", year=2003
    def parse_col(col):
        match = re.search(r'^(.*)\s+\((\d{4})\)$', col)
        if match:
            return match.group(1), int(match.group(2))
        return col, None

    melted[['Indicator', 'Tahun']] = melted['Raw_Col'].apply(lambda x: pd.Series(parse_col(x)))
    
    # Map indicators to cleaner names if map provided
    if indicator_map:
        melted['Indicator'] = melted['Indicator'].map(lambda x: indicator_map.get(x, x))
    
    # Pivot back so indicators are columns but Year is a row
    long_df = melted.pivot_table(index=['Provinsi', 'Tahun'], columns='Indicator', values='Value').reset_index()
    return long_df

# 1. Process APM
apm_map = {
    'SD/sederajat': 'APM_SD',
    'SMP/sederajat': 'APM_SMP',
    'SM/sederajat': 'APM_SMA'
}
df_apm = process_to_long('dataset/APM_final.csv', apm_map)

# 2. Process PPK
df_ppk = process_to_long('dataset/PPK_final.csv')
df_ppk.rename(columns={'PPK': 'PPK'}, inplace=True)

# 3. Process PSN
df_psn = process_to_long('dataset/PSN_final.csv')
df_psn.rename(columns={'PSN': 'PSN (Stunting)'}, inplace=True)

# 4. Process RLS
rls_map = {'rata_rata_lama_sekolah': 'RLS'}
df_rls = process_to_long('dataset/RLS_final.csv', rls_map)

# 5. Process IPM
ipm_map = {
    'IPM Laki-laki': 'IPM_Laki_Laki',
    'IPM Perempuan': 'IPM_Perempuan'
}
df_ipm = process_to_long('dataset/IPM_final.csv', ipm_map)

# Merge all
final_df = df_apm.merge(df_ppk, on=['Provinsi', 'Tahun'], how='outer')
final_df = final_df.merge(df_psn, on=['Provinsi', 'Tahun'], how='outer')
final_df = final_df.merge(df_rls, on=['Provinsi', 'Tahun'], how='outer')
final_df = final_df.merge(df_ipm, on=['Provinsi', 'Tahun'], how='outer')

# Sort
final_df = final_df.sort_values(by=['Tahun', 'Provinsi'])

# Reorder columns to match user example
cols = ['Tahun', 'Provinsi', 'APM_SD', 'APM_SMP', 'APM_SMA', 'IPM_Laki_Laki', 'IPM_Perempuan', 'PPK', 'PSN (Stunting)', 'RLS']
# Filter columns that exist
existing_cols = [c for c in cols if c in final_df.columns]
final_df = final_df[existing_cols]

# Save
output_path = 'dataset/integrated.csv'
final_df.to_csv(output_path, index=False)

print(f"Successfully created integrated long format at {output_path}")
print(final_df.head(10))
