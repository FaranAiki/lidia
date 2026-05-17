# Analysis Report: integrated_apm_ipm_ppk

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

          APM_SD    APM_SMP    APM_SMA  IPM_Laki_Laki  IPM_Perempuan           PPK
count  38.000000  38.000000  38.000000      38.000000      38.000000     38.000000
mean   95.092105  77.339737  64.423947      78.008947      71.412632  11962.473684
std     5.490588   7.456689   9.014287       4.665866       6.197836   2543.098384
min    72.550000  54.330000  35.590000      59.650000      52.390000   5861.000000
25%    95.675000  75.070000  61.525000      77.102500      69.697500  10598.250000
50%    96.390000  78.470000  65.610000      78.605000      72.140000  11977.500000
75%    97.547500  81.467500  70.245000      79.880000      74.237500  12766.250000
max    98.770000  88.670000  78.420000      86.840000      84.170000  20676.000000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                 APM_SD   APM_SMP   APM_SMA  IPM_Laki_Laki  IPM_Perempuan       PPK
APM_SD         1.000000  0.870730  0.855871       0.853901       0.820953  0.613113
APM_SMP        0.870730  1.000000  0.917955       0.856658       0.882136  0.700294
APM_SMA        0.855871  0.917955  1.000000       0.821249       0.856651  0.663433
IPM_Laki_Laki  0.853901  0.856658  0.821249       1.000000       0.929397  0.844164
IPM_Perempuan  0.820953  0.882136  0.856651       0.929397       1.000000  0.852523
PPK            0.613113  0.700294  0.663433       0.844164       0.852523  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.8439 
  *(Interpretasi: 84.39% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.2129 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.1533 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SD** diprediksi akan **naik** sebesar 0.7856 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SD** diprediksi akan **naik** sebesar 0.0082 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SD** diprediksi akan **turun** sebesar 0.0007 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8893 
  *(Interpretasi: 88.93% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.2785 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.4000 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SMP** diprediksi akan **naik** sebesar 0.0802 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SMP** diprediksi akan **naik** sebesar 0.3202 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMP** diprediksi akan **turun** sebesar 0.0000 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8639 
  *(Interpretasi: 86.39% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.3603 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.7186 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SMA** diprediksi akan **turun** sebesar 0.2064 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SMA** diprediksi akan **naik** sebesar 0.4181 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMA** diprediksi akan **turun** sebesar 0.0001 unit.

### Target: IPM_Laki_Laki
**Predictive (Model Fit):**
- **R-squared**: 0.9129 
  *(Interpretasi: 91.29% varians dari IPM_Laki_Laki dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Laki_Laki, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.3166 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.0247 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **IPM_Laki_Laki** diprediksi akan **turun** sebesar 0.0354 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.2955 unit.
- Setiap kenaikan 1 unit pada **PPK**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.0005 unit.

### Target: IPM_Perempuan
**Predictive (Model Fit):**
- **R-squared**: 0.9163 
  *(Interpretasi: 91.63% varians dari IPM_Perempuan dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Perempuan, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.0056 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.1673 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.1216 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.5011 unit.
- Setiap kenaikan 1 unit pada **PPK**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.0007 unit.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.8032 
  *(Interpretasi: 80.32% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PPK** diprediksi akan **turun** sebesar 191.4804 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PPK** diprediksi akan **turun** sebesar 9.3637 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PPK** diprediksi akan **turun** sebesar 17.2474 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **PPK** diprediksi akan **naik** sebesar 367.9429 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **PPK** diprediksi akan **naik** sebesar 263.0540 unit.

