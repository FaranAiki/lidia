import pandas as pd
import glob
import os
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

def perform_extra_analysis(file_path):
    print(f"Analisis Tambahan: {file_path}")
    df = pd.read_csv(file_path)
    numeric_df = df.select_dtypes(include=['number']).drop(columns=['Tahun'], errors='ignore')
    
    results = [f"# Analisis Statistik Lanjutan: {os.path.basename(file_path)}\n"]
    
    # 1. Matriks Korelasi (Pearson)
    results.append("## 1. Hubungan antar Variabel (Korelasi Pearson)")
    corr_matrix = numeric_df.corr()
    results.append("Menunjukkan seberapa kuat hubungan antar indikator (1.0 = Sangat Kuat, 0 = Tidak Ada).\n")
    results.append("```")
    results.append(corr_matrix.to_string())
    results.append("```\n")

    # 2. Uji Gender Gap (T-Test) - Jika ada data Laki-laki & Perempuan
    if 'IPM_Laki_Laki' in df.columns and 'IPM_Perempuan' in df.columns:
        results.append("## 2. Analisis Ketimpangan Gender (Paired T-Test)")
        # Menghapus baris yang memiliki NaN pada kolom IPM
        clean_df = df[['IPM_Laki_Laki', 'IPM_Perempuan']].dropna()
        t_stat, p_val = stats.ttest_rel(clean_df['IPM_Laki_Laki'], clean_df['IPM_Perempuan'])
        
        results.append(f"- **T-Statistic:** {t_stat:.4f}")
        results.append(f"- **p-value:** {p_val:.4e}")
        if p_val < 0.05:
            gap = clean_df['IPM_Laki_Laki'].mean() - clean_df['IPM_Perempuan'].mean()
            results.append(f"  - **Kesimpulan:** Ada perbedaan signifikan (Gender Gap) sebesar {gap:.2f} poin antara Laki-laki dan Perempuan.")
        else:
            results.append("  - **Kesimpulan:** Tidak ada perbedaan signifikan secara statistik antara Laki-laki dan Perempuan.")
        results.append("\n")

    # 3. Statistik Deskriptif (Rata-rata, Min, Max)
    results.append("## 3. Ringkasan Statistik (Deskriptif)")
    results.append("```")
    results.append(numeric_df.describe().to_string())
    results.append("```\n")
    
    return "\n".join(results)

def main():
    files = glob.glob('partial_dataset/*.csv')
    if not os.path.exists('output'): os.makedirs('output')
    
    for file in sorted(files):
        report = perform_extra_analysis(file)
        base_name = os.path.basename(file).replace('.csv', '')
        with open(f'output/extra_stats_{base_name}.md', 'w') as f:
            f.write(report)

if __name__ == "__main__":
    main()
