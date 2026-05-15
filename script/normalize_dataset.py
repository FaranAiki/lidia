import pandas as pd
import os
import re

def normalize_province_name(name):
    if not isinstance(name, str):
        return ""
    name = name.strip().upper()
    # Remove "PROVINSI " prefix if exists
    name = re.sub(r'^PROVINSI\s+', '', name)
    # Common mappings
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

# Load provinces
with open('dataset/daftar_provinsi.txt', 'r') as f:
    provinces_raw = [line.strip() for line in f if line.strip()]

provinces_norm = {normalize_province_name(p): p for p in provinces_raw}

def process_csv(filename, header_row, location_col):
    filepath = os.path.join('dataset', filename)
    print(f"Processing {filepath}...")
    
    # Read the file
    # We might need to read it differently depending on the file
    if filename == 'IPM.csv':
        # IPM.csv has a very messy header
        df = pd.read_csv(filepath, skiprows=4, header=None)
        # We need to preserve some header info? The user just said normalize/filter.
        # Let's try to keep the data rows.
        # But we need to output it with the original header?
        # Actually, if we just want the data, let's just use the rows we found.
        # But the output should be a valid CSV.
        
        # Let's read the header separately to preserve it if possible
        with open(filepath, 'r') as f:
            header_lines = [f.readline() for _ in range(4)]
        
        df.columns = ['Location', 'Laki-laki', 'Perempuan']
    elif filename == 'PPK.csv':
        with open(filepath, 'r') as f:
            header_lines = [f.readline() for _ in range(3)]
        df = pd.read_csv(filepath, skiprows=3, header=None)
        # Columns are Location, 2016-2025
        df.columns = ['Location'] + [str(year) for year in range(2016, 2026)]
    elif filename == 'APM.csv':
        df = pd.read_csv(filepath)
        header_lines = [] # Standard CSV
        location_col = 'Provinsi'
    elif filename == 'PSN.csv':
        with open(filepath, 'r') as f:
            header_lines = [f.readline() for _ in range(2)]
        df = pd.read_csv(filepath, skiprows=2, header=None)
        # PSN.csv header row 1 is: Provinsi,2020,2021,2022,2023
        df.columns = ['Provinsi', '2020', '2021', '2022', '2023']
        location_col = 'Provinsi'
    elif filename == 'RLS.csv':
        df = pd.read_csv(filepath)
        header_lines = []
        location_col = 'nama_provinsi'
    else:
        return

    # Filtering
    def is_province(name):
        if not isinstance(name, str):
            return False
        # Check if the name is all caps (ignoring non-alphabetic characters)
        # BPS provinces are always uppercase in these files.
        if name != name.upper():
            return False
        
        norm = normalize_province_name(name)
        return norm in provinces_norm

    if 'Location' in df.columns:
        col = 'Location'
    else:
        col = location_col

    df_filtered = df[df[col].apply(is_province)].copy()
    
    # Optional: Normalize the name to the official one? 
    # The user didn't ask for it, but it might be cleaner.
    # df_filtered[col] = df_filtered[col].apply(lambda x: provinces_norm[normalize_province_name(x)])

    # Write output
    output_filename = filename.replace('.csv', '_province.csv')
    output_path = os.path.join('dataset', output_filename)
    
    with open(output_path, 'w') as f:
        for line in header_lines:
            f.write(line)
        df_filtered.to_csv(f, index=False, header=(len(header_lines) == 0))
    
    print(f"Saved to {output_path}")

# Process files
files_to_process = [
    ('APM.csv', 0, 'Provinsi'),
    ('IPM.csv', 4, 0),
    ('PPK.csv', 3, 0),
    ('PSN.csv', 2, 'Provinsi'),
    ('RLS.csv', 0, 'nama_provinsi')
]

for filename, skip, col in files_to_process:
    process_csv(filename, skip, col)
