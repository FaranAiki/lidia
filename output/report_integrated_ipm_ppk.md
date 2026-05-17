# Analysis Report: integrated_ipm_ppk

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

       IPM_Laki_Laki  IPM_Perempuan           PPK
count      38.000000      38.000000     38.000000
mean       78.008947      71.412632  11962.473684
std         4.665866       6.197836   2543.098384
min        59.650000      52.390000   5861.000000
25%        77.102500      69.697500  10598.250000
50%        78.605000      72.140000  11977.500000
75%        79.880000      74.237500  12766.250000
max        86.840000      84.170000  20676.000000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

               IPM_Laki_Laki  IPM_Perempuan       PPK
IPM_Laki_Laki       1.000000       0.929397  0.844164
IPM_Perempuan       0.929397       1.000000  0.852523
PPK                 0.844164       0.852523  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: IPM_Laki_Laki
**Predictive (Model Fit):**
- **R-squared**: 0.8736 
  *(Interpretasi: 87.36% varians dari IPM_Laki_Laki dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Laki_Laki, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.5779 unit.
- Setiap kenaikan 1 unit pada **PPK**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.0003 unit.

### Target: IPM_Perempuan
**Predictive (Model Fit):**
- **R-squared**: 0.8798 
  *(Interpretasi: 87.98% varians dari IPM_Perempuan dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Perempuan, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.9694 unit.
- Setiap kenaikan 1 unit pada **PPK**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.0006 unit.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.7465 
  *(Interpretasi: 74.65% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **PPK** diprediksi akan **naik** sebesar 207.3893 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **PPK** diprediksi akan **naik** sebesar 204.7033 unit.

