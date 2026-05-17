# Analysis Report: integrated_filled

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA  IPM_Laki_Laki  IPM_Perempuan           PPK  PSN (Stunting)         RLS
count  874.000000  874.000000  874.000000     874.000000     874.000000    874.000000      874.000000  874.000000
mean    93.130732   69.417185   52.528970      78.008947      71.412632   9279.103478       20.427483    7.717632
std      6.803774   11.508673   13.268452       4.606699       6.119244   2795.311537       17.937744    1.475459
min     65.870000   33.880000    8.620000      59.650000      52.390000    677.670000        0.000000    1.610000
25%     92.182500   63.055000   43.232500      77.100000      69.510000   7552.522500        7.910000    6.910000
50%     94.720000   71.370000   55.350000      78.605000      72.140000   9176.135000       16.085000    7.820000
75%     97.530000   78.337500   62.615000      79.890000      74.350000  10914.250000       27.090000    8.657500
max     99.590000   90.140000   78.420000      86.840000      84.170000  20676.000000      100.000000   11.580000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                  APM_SD   APM_SMP   APM_SMA  IPM_Laki_Laki  IPM_Perempuan       PPK  PSN (Stunting)       RLS
APM_SD          1.000000  0.818251  0.759592       0.722346       0.709536  0.649014       -0.071862  0.725899
APM_SMP         0.818251  1.000000  0.930445       0.644338       0.670511  0.755130       -0.270192  0.789696
APM_SMA         0.759592  0.930445  1.000000       0.590066       0.609784  0.713014       -0.301835  0.822623
IPM_Laki_Laki   0.722346  0.644338  0.590066       1.000000       0.929397  0.708868       -0.099112  0.763936
IPM_Perempuan   0.709536  0.670511  0.609784       0.929397       1.000000  0.727564       -0.117884  0.733035
PPK             0.649014  0.755130  0.713014       0.708868       0.727564  1.000000       -0.399432  0.798844
PSN (Stunting) -0.071862 -0.270192 -0.301835      -0.099112      -0.117884 -0.399432        1.000000 -0.336646
RLS             0.725899  0.789696  0.822623       0.763936       0.733035  0.798844       -0.336646  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7536 
  *(Interpretasi: 75.36% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.3739 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.0062 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SD** diprediksi akan **naik** sebesar 0.4701 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SD** diprediksi akan **turun** sebesar 0.0167 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SD** diprediksi akan **turun** sebesar 0.0001 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SD** diprediksi akan **naik** sebesar 0.0510 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SD** diprediksi akan **naik** sebesar 0.3594 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.9083 
  *(Interpretasi: 90.83% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.3982 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.6210 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SMP** diprediksi akan **turun** sebesar 0.0792 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SMP** diprediksi akan **naik** sebesar 0.1433 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMP** diprediksi akan **naik** sebesar 0.0007 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMP** diprediksi akan **turun** sebesar 0.0078 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMP** diprediksi akan **turun** sebesar 1.0574 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8996 
  *(Interpretasi: 89.96% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.0096 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.9038 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **APM_SMA** diprediksi akan **turun** sebesar 0.4589 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **APM_SMA** diprediksi akan **naik** sebesar 0.0272 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMA** diprediksi akan **turun** sebesar 0.0004 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMA** diprediksi akan **turun** sebesar 0.0078 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMA** diprediksi akan **naik** sebesar 3.3612 unit.

### Target: IPM_Laki_Laki
**Predictive (Model Fit):**
- **R-squared**: 0.8929 
  *(Interpretasi: 89.29% varians dari IPM_Laki_Laki dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Laki_Laki, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.0937 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **IPM_Laki_Laki** diprediksi akan **turun** sebesar 0.0148 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **IPM_Laki_Laki** diprediksi akan **turun** sebesar 0.0590 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.5582 unit.
- Setiap kenaikan 1 unit pada **PPK**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.0000 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.0102 unit.
- Setiap kenaikan 1 unit pada **RLS**, **IPM_Laki_Laki** diprediksi akan **naik** sebesar 0.9231 unit.

### Target: IPM_Perempuan
**Predictive (Model Fit):**
- **R-squared**: 0.8781 
  *(Interpretasi: 87.81% varians dari IPM_Perempuan dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) IPM_Perempuan, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **IPM_Perempuan** diprediksi akan **turun** sebesar 0.0067 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.0538 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.0070 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **IPM_Perempuan** diprediksi akan **naik** sebesar 1.1207 unit.
- Setiap kenaikan 1 unit pada **PPK**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.0003 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **IPM_Perempuan** diprediksi akan **naik** sebesar 0.0058 unit.
- Setiap kenaikan 1 unit pada **RLS**, **IPM_Perempuan** diprediksi akan **turun** sebesar 0.4106 unit.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.7440 
  *(Interpretasi: 74.40% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PPK** diprediksi akan **turun** sebesar 25.7404 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PPK** diprediksi akan **naik** sebesar 110.0314 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PPK** diprediksi akan **turun** sebesar 43.5564 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **PPK** diprediksi akan **naik** sebesar 12.2279 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **PPK** diprediksi akan **naik** sebesar 127.4626 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **PPK** diprediksi akan **turun** sebesar 28.4765 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PPK** diprediksi akan **naik** sebesar 710.8413 unit.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.3003 
  *(Interpretasi: 30.03% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PSN (Stunting)** diprediksi akan **naik** sebesar 1.0075 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.1441 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.0995 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **PSN (Stunting)** diprediksi akan **naik** sebesar 1.0131 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.2842 unit.
- Setiap kenaikan 1 unit pada **PPK**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.0032 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PSN (Stunting)** diprediksi akan **turun** sebesar 4.2712 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.8327 
  *(Interpretasi: 83.27% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **RLS** diprediksi akan **naik** sebesar 0.0115 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **RLS** diprediksi akan **turun** sebesar 0.0317 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **RLS** diprediksi akan **naik** sebesar 0.0692 unit.
- Setiap kenaikan 1 unit pada **IPM_Laki_Laki**, **RLS** diprediksi akan **naik** sebesar 0.1479 unit.
- Setiap kenaikan 1 unit pada **IPM_Perempuan**, **RLS** diprediksi akan **turun** sebesar 0.0328 unit.
- Setiap kenaikan 1 unit pada **PPK**, **RLS** diprediksi akan **naik** sebesar 0.0001 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **RLS** diprediksi akan **turun** sebesar 0.0069 unit.

