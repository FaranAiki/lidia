# Analysis Report: integrated_apm_psn

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA  PSN (Stunting)
count  152.000000  152.000000  152.000000      152.000000
mean    95.516316   76.351579   60.627829       10.019737
std      6.512357    8.990834    9.387800        5.862102
min     71.030000   49.680000   29.460000        0.100000
25%     95.807500   73.530000   58.445000        5.450000
50%     97.985000   78.630000   61.420000        9.150000
75%     98.660000   82.075000   65.960000       13.100000
max     99.590000   88.210000   76.370000       28.700000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                  APM_SD   APM_SMP   APM_SMA  PSN (Stunting)
APM_SD          1.000000  0.865300  0.814589       -0.029268
APM_SMP         0.865300  1.000000  0.892279       -0.195576
APM_SMA         0.814589  0.892279  1.000000       -0.098321
PSN (Stunting) -0.029268 -0.195576 -0.098321        1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7741 
  *(Interpretasi: 77.41% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.5430 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.1102 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SD** diprediksi akan **naik** sebesar 0.1477 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8700 
  *(Interpretasi: 87.00% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.5955 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.5057 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMP** diprediksi akan **turun** sebesar 0.2010 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8065 
  *(Interpretasi: 80.65% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.1961 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.8209 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMA** diprediksi akan **naik** sebesar 0.0952 unit.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.1302 
  *(Interpretasi: 13.02% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.4608 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.5717 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.1668 unit.

