import pandas as pd
import os
from itertools import combinations

def create_all_partial_combinations():
    input_file = 'dataset/integrated.csv'
    output_dir = 'partial_dataset'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        # Clean existing files in the directory to avoid confusion
        for file in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, file))
        
    df = pd.read_csv(input_file)
    
    # Define column groups
    groups = {
        'apm': ['APM_SD', 'APM_SMP', 'APM_SMA'],
        'ipm': ['IPM_Laki_Laki', 'IPM_Perempuan'],
        'ppk': ['PPK'],
        'psn': ['PSN (Stunting)'],
        'rls': ['RLS']
    }
    
    indicator_names = list(groups.keys())
    
    # Combinations of sizes 2, 3, and 4
    for r in range(2, 5):
        for combo in combinations(indicator_names, r):
            # Build column list
            current_cols = ['Tahun', 'Provinsi']
            for name in combo:
                current_cols.extend(groups[name])
            
            # Filter and drop missing values
            partial_df = df[current_cols].dropna()
            
            # Only save if there's data left
            if not partial_df.empty:
                combo_name = "_".join(combo)
                output_file = os.path.join(output_dir, f'integrated_{combo_name}.csv')
                partial_df.to_csv(output_file, index=False)
                print(f"Created {output_file} with {len(partial_df)} rows.")
            else:
                print(f"Skipped {combo} - No complete data found for this combination.")

if __name__ == "__main__":
    create_all_partial_combinations()
