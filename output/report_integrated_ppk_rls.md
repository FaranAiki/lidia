# Analysis Report: integrated_ppk_rls

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

                PPK         RLS
count    342.000000  342.000000
mean   10472.853801    8.368012
std     2473.333255    1.296048
min     3770.000000    3.220000
25%     8961.250000    7.780000
50%    10400.500000    8.460000
75%    11618.750000    9.172500
max    19953.000000   11.490000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

          PPK       RLS
PPK  1.000000  0.724789
RLS  0.724789  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.5253 
  *(Interpretasi: 52.53% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **RLS**, **PPK** diprediksi akan **naik** sebesar 1383.1615 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.5253 
  *(Interpretasi: 52.53% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **PPK**, **RLS** diprediksi akan **naik** sebesar 0.0004 unit.

