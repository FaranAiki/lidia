import pandas as pd
import glob
import os
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

def perform_anova(file_path):
    print(f"Analyzing: {file_path}")
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        return f"Error reading {file_path}: {e}"
    
    # Ensure Tahun and Provinsi are treated as categories
    if 'Tahun' in df.columns:
        df['Tahun'] = df['Tahun'].astype(str)
    if 'Provinsi' in df.columns:
        df['Provinsi'] = df['Provinsi'].astype(str)
        
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    results = []
    results.append(f"# Analisis ANOVA untuk {os.path.basename(file_path)}\n")
    
    num_years = df['Tahun'].nunique() if 'Tahun' in df.columns else 0
    num_provinces = df['Provinsi'].nunique() if 'Provinsi' in df.columns else 0
    
    results.append(f"**Informasi Dataset:**")
    results.append(f"- Jumlah Tahun: {num_years}")
    results.append(f"- Jumlah Provinsi: {num_provinces}")
    results.append("")

    for col in numeric_cols:
        results.append(f"## Variabel: {col}")
        
        # 1. One-Way ANOVA by Tahun (Membandingkan rata-rata antar tahun)
        if num_years > 1:
            # Grouping by year, dropping NaNs for each group
            groups = [group[col].dropna() for name, group in df.groupby('Tahun')]
            # Only perform if we have at least 2 groups and each group has data
            if len(groups) > 1 and all(len(g) > 0 for g in groups):
                f_stat, p_val = stats.f_oneway(*groups)
                results.append(f"### 1. Perbedaan antar Tahun (One-Way ANOVA)")
                results.append(f"- **F-Statistic:** {f_stat:.4f}")
                results.append(f"- **p-value:** {p_val:.4e}")
                if p_val < 0.05:
                    results.append("  - **Kesimpulan:** Ada perbedaan signifikan antar tahun. Tren waktu berpengaruh nyata.")
                else:
                    results.append("  - **Kesimpulan:** Tidak ada perbedaan signifikan antar tahun. Indikator cenderung stabil.")
            else:
                results.append("- *One-Way ANOVA (Tahun) tidak dapat dilakukan karena data tidak cukup.*")

        # 2. One-Way ANOVA by Provinsi (Membandingkan rata-rata antar provinsi)
        if num_provinces > 1:
            # Check if we have multiple entries per province (multiple years)
            counts = df.groupby('Provinsi')[col].count()
            if counts.min() > 1:
                groups = [group[col].dropna() for name, group in df.groupby('Provinsi')]
                if len(groups) > 1 and all(len(g) > 0 for g in groups):
                    f_stat, p_val = stats.f_oneway(*groups)
                    results.append(f"### 2. Perbedaan antar Provinsi (One-Way ANOVA)")
                    results.append(f"- **F-Statistic:** {f_stat:.4f}")
                    results.append(f"- **p-value:** {p_val:.4e}")
                    if p_val < 0.05:
                        results.append("  - **Kesimpulan:** Ada perbedaan signifikan antar provinsi. Kesenjangan antar wilayah nyata.")
                    else:
                        results.append("  - **Kesimpulan:** Tidak ada perbedaan signifikan antar provinsi. Kondisi relatif merata.")
            else:
                results.append(f"### 2. Perbedaan antar Provinsi")
                results.append("- *One-Way ANOVA (Provinsi) memerlukan lebih dari 1 tahun data untuk setiap provinsi.*")
        
        results.append("\n" + "-"*30 + "\n")
        
    return "\n".join(results)

def main():
    files = glob.glob('partial_dataset/*.csv')
    if not os.path.exists('output'):
        os.makedirs('output')
        
    summary_report = []
    
    for file in sorted(files):
        report = perform_anova(file)
        summary_report.append(report)
        
        # Save individual report
        base_name = os.path.basename(file).replace('.csv', '')
        with open(f'output/anova_{base_name}.md', 'w') as f:
            f.write(report)
            
    # Save combined report
    with open('output/anova_summary_all.md', 'w') as f:
        f.write("# Laporan Ringkasan Analisis ANOVA\n\n")
        f.write("Laporan ini berisi hasil uji ANOVA untuk semua kombinasi variabel.\n\n")
        f.write("\n\n".join(summary_report))
    
    print(f"Selesai! Hasil disimpan di folder 'output/'")

if __name__ == "__main__":
    main()
