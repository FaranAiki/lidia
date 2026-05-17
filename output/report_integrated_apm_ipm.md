# Analysis Report: integrated_apm_ipm

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

          APM_SD    APM_SMP    APM_SMA  IPM_Laki_Laki  IPM_Perempuan
count  38.000000  38.000000  38.000000      38.000000      38.000000
mean   95.092105  77.339737  64.423947      78.008947      71.412632
std     5.490588   7.456689   9.014287       4.665866       6.197836
min    72.550000  54.330000  35.590000      59.650000      52.390000
25%    95.675000  75.070000  61.525000      77.102500      69.697500
50%    96.390000  78.470000  65.610000      78.605000      72.140000
75%    97.547500  81.467500  70.245000      79.880000      74.237500
max    98.770000  88.670000  78.420000      86.840000      84.170000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                 APM_SD   APM_SMP   APM_SMA  IPM_Laki_Laki  IPM_Perempuan
APM_SD         1.000000  0.870730  0.855871       0.853901       0.820953
APM_SMP        0.870730  1.000000  0.917955       0.856658       0.882136
APM_SMA        0.855871  0.917955  1.000000       0.821249       0.856651
IPM_Laki_Laki  0.853901  0.856658  0.821249       1.000000       0.929397
IPM_Perempuan  0.820953  0.882136  0.856651       0.929397       1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.8194 
  *(Interpretasi: 81.94% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.2540 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.1915 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SD** diprediksi akan **naik** sebesar 0.6075 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SD** diprediksi akan **turun** sebesar 0.2060 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8893 
  *(Interpretasi: 88.93% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.2872 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.4009 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SMP** diprediksi akan **naik** sebesar 0.0636 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SMP** diprediksi akan **naik** sebesar 0.3084 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8636 
  *(Interpretasi: 86.36% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.3899 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.7218 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SMA** diprediksi akan **turun** sebesar 0.2622 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SMA** diprediksi akan **naik** sebesar 0.3797 unit.

### Target: IPM_Laki_Laki
**Predictive (Model Fit):**
- **R-squared**: 0.8909 
  *(Interpretasi: 89.09% varians dari IPM_Laki_Laki dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Laki_Laki, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.2652 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.0245 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **IPM_Laki_Laki** diprediksi akan **turun** sebesar 0.0562 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.5508 unit.

### Target: IPM_Perempuan
**Predictive (Model Fit):**
- **R-squared**: 0.8985 
  *(Interpretasi: 89.85% varians dari IPM_Perempuan dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Perempuan, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **IPM_Perempuan** diprediksi akan **turun** sebesar 0.1475 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.1952 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.1335 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.9036 unit.

