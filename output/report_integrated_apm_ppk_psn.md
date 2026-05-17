# Analysis Report: integrated_apm_ppk_psn

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA           PPK  PSN (Stunting)
count  152.000000  152.000000  152.000000    152.000000      152.000000
mean    95.516316   76.351579   60.627829  10622.703947       10.019737
std      6.512357    8.990834    9.387800   2427.831793        5.862102
min     71.030000   49.680000   29.460000   4700.000000        0.100000
25%     95.807500   73.530000   58.445000   9164.250000        5.450000
50%     97.985000   78.630000   61.420000  10678.000000        9.150000
75%     98.660000   82.075000   65.960000  11698.000000       13.100000
max     99.590000   88.210000   76.370000  19373.000000       28.700000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                  APM_SD   APM_SMP   APM_SMA       PPK  PSN (Stunting)
APM_SD          1.000000  0.865300  0.814589  0.601733       -0.029268
APM_SMP         0.865300  1.000000  0.892279  0.681253       -0.195576
APM_SMA         0.814589  0.892279  1.000000  0.550540       -0.098321
PPK             0.601733  0.681253  0.550540  1.000000       -0.380187
PSN (Stunting) -0.029268 -0.195576 -0.098321 -0.380187        1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7804 
  *(Interpretasi: 78.04% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.4751 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.1256 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SD** diprediksi akan **naik** sebesar 0.0003 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SD** diprediksi akan **naik** sebesar 0.1790 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8831 
  *(Interpretasi: 88.31% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.4820 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.4901 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMP** diprediksi akan **naik** sebesar 0.0006 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMP** diprediksi akan **turun** sebesar 0.1130 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8107 
  *(Interpretasi: 81.07% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.2249 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.8654 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMA** diprediksi akan **turun** sebesar 0.0004 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMA** diprediksi akan **naik** sebesar 0.0511 unit.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.5477 
  *(Interpretasi: 54.77% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PPK** diprediksi akan **naik** sebesar 89.4145 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PPK** diprediksi akan **naik** sebesar 168.6519 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PPK** diprediksi akan **turun** sebesar 59.2248 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **PPK** diprediksi akan **turun** sebesar 113.2865 unit.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.2396 
  *(Interpretasi: 23.96% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.5021 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.3125 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.0800 unit.
- Setiap kenaikan 1 unit pada **PPK**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.0011 unit.

