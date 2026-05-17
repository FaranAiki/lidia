import pandas as pd
import numpy as np
import os

def simple_linear_regression(X, y):
    # Add intercept
    X_mat = np.column_stack((np.ones(len(X)), X.values))
    # Calculate coefficients: (X^T * X)^-1 * X^T * y
    try:
        beta = np.linalg.inv(X_mat.T.dot(X_mat)).dot(X_mat.T).dot(y.values)
        # Calculate R-squared
        y_pred = X_mat.dot(beta)
        ss_tot = np.sum((y.values - np.mean(y.values)) ** 2)
        ss_res = np.sum((y.values - y_pred) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        return beta[1:], r2 # Exclude intercept for coefficients
    except np.linalg.LinAlgError:
        return np.zeros(X.shape[1]), 0

def analyze_dataset(file_path, output_dir, name):
    df = pd.read_csv(file_path)
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Exclude 'Tahun' from analysis
    if 'Tahun' in numeric_df.columns:
        numeric_df = numeric_df.drop(columns=['Tahun'])
        
    if numeric_df.empty or numeric_df.shape[1] < 2:
        return

    # Drop any remaining NaNs for analysis
    numeric_df = numeric_df.dropna()
    
    if len(numeric_df) < 5:
        return

    report_path = os.path.join(output_dir, f"report_{name}.md")
    
    with open(report_path, 'w') as f:
        f.write(f"# Analysis Report: {name}\n\n")
        
        # 1. Descriptive
        f.write("## 1. Descriptive Analysis\n")
        f.write("Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.\n\n")
        f.write(numeric_df.describe().to_string())
        f.write("\n\n")
        
        # 2. Diagnostic
        f.write("## 2. Diagnostic Analysis\n")
        f.write("Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.\n\n")
        f.write(numeric_df.corr().to_string())
        f.write("\n\n")
        
        # 3. Predictive & 4. Prescriptive
        f.write("## 3. Predictive & 4. Prescriptive Analysis\n")
        f.write("Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.\n\n")
        
        for target in numeric_df.columns:
            y = numeric_df[target]
            X = numeric_df.drop(columns=[target])
            
            coefs, r2 = simple_linear_regression(X, y)
            
            f.write(f"### Target: {target}\n")
            f.write(f"**Predictive (Model Fit):**\n")
            f.write(f"- **R-squared**: {r2:.4f} \n")
            f.write(f"  *(Interpretasi: {r2*100:.2f}% varians dari {target} dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*\n\n")
            
            f.write(f"**Prescriptive (Actionable Insights):**\n")
            f.write(f"Untuk mengoptimalkan (menaikkan/menurunkan) {target}, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):\n")
            for col, coef in zip(X.columns, coefs):
                direction = "naik" if coef > 0 else "turun"
                f.write(f"- Setiap kenaikan 1 unit pada **{col}**, **{target}** diprediksi akan **{direction}** sebesar {abs(coef):.4f} unit.\n")
            f.write("\n")

def main():
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    datasets = [
        ('dataset/integrated_filled.csv', 'integrated_filled')
    ]
    
    partial_dir = 'partial_dataset'
    if os.path.exists(partial_dir):
        for file in os.listdir(partial_dir):
            if file.endswith('.csv'):
                datasets.append((os.path.join(partial_dir, file), file.replace('.csv', '')))
                
    for path, name in datasets:
        if os.path.exists(path):
            analyze_dataset(path, output_dir, name)
            print(f"Generated report for {name}")

if __name__ == '__main__':
    main()
