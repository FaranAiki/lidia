# Analysis Report: integrated_apm_ppk

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA           PPK
count  380.000000  380.000000  380.000000    380.000000
mean    95.259579   75.752921   60.618526  10621.815789
std      6.478123    9.066143    9.753535   2517.069066
min     69.030000   45.960000   24.560000   3770.000000
25%     95.672500   73.127500   57.895000   9075.750000
50%     97.635000   78.060000   62.490000  10578.000000
75%     98.417500   81.355000   66.370000  11902.750000
max     99.590000   90.140000   78.420000  20676.000000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

           APM_SD   APM_SMP   APM_SMA       PPK
APM_SD   1.000000  0.855953  0.810501  0.594310
APM_SMP  0.855953  1.000000  0.898446  0.693660
APM_SMA  0.810501  0.898446  1.000000  0.593946
PPK      0.594310  0.693660  0.593946  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7417 
  *(Interpretasi: 74.17% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.4656 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.1442 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SD** diprediksi akan **naik** sebesar 0.0000 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8776 
  *(Interpretasi: 87.76% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.4321 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.4958 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMP** diprediksi akan **naik** sebesar 0.0007 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8153 
  *(Interpretasi: 81.53% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.2338 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.8658 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMA** diprediksi akan **turun** sebesar 0.0002 unit.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.4858 
  *(Interpretasi: 48.58% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PPK** diprediksi akan **naik** sebesar 10.3241 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PPK** diprediksi akan **naik** sebesar 225.5646 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PPK** diprediksi akan **turun** sebesar 40.6547 unit.

