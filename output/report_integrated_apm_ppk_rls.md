# Analysis Report: integrated_apm_ppk_rls

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA           PPK         RLS
count  342.000000  342.000000  342.000000    342.000000  342.000000
mean    95.278187   75.576608   60.195702  10472.853801    8.368012
std      6.585449    9.220068    9.753091   2473.333255    1.296048
min     69.030000   45.960000   24.560000   3770.000000    3.220000
25%     95.680000   72.712500   57.830000   8961.250000    7.780000
50%     97.740000   77.915000   61.535000  10400.500000    8.460000
75%     98.475000   81.275000   65.742500  11618.750000    9.172500
max     99.590000   90.140000   77.860000  19953.000000   11.490000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

           APM_SD   APM_SMP   APM_SMA       PPK       RLS
APM_SD   1.000000  0.857046  0.815848  0.605940  0.705128
APM_SMP  0.857046  1.000000  0.899175  0.696757  0.736507
APM_SMA  0.815848  0.899175  1.000000  0.577242  0.763553
PPK      0.605940  0.696757  0.577242  1.000000  0.724789
RLS      0.705128  0.736507  0.763553  0.724789  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7516 
  *(Interpretasi: 75.16% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.4512 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.1057 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SD** diprediksi akan **turun** sebesar 0.0001 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SD** diprediksi akan **naik** sebesar 0.7030 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8845 
  *(Interpretasi: 88.45% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.4114 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.5650 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMP** diprediksi akan **naik** sebesar 0.0009 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMP** diprediksi akan **turun** sebesar 0.7935 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8552 
  *(Interpretasi: 85.52% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.1351 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.7922 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMA** diprediksi akan **turun** sebesar 0.0009 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMA** diprediksi akan **naik** sebesar 2.3387 unit.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.6383 
  *(Interpretasi: 63.83% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PPK** diprediksi akan **turun** sebesar 13.5844 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PPK** diprediksi akan **naik** sebesar 213.7446 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PPK** diprediksi akan **turun** sebesar 142.6185 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PPK** diprediksi akan **naik** sebesar 1131.3925 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.7150 
  *(Interpretasi: 71.50% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **RLS** diprediksi akan **naik** sebesar 0.0312 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **RLS** diprediksi akan **turun** sebesar 0.0387 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **RLS** diprediksi akan **naik** sebesar 0.0813 unit.
- Setiap kenaikan 1 unit pada **PPK**, **RLS** diprediksi akan **naik** sebesar 0.0002 unit.

