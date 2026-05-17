# Analysis Report: integrated_apm_ppk_psn_rls

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA           PPK  PSN (Stunting)         RLS
count  152.000000  152.000000  152.000000    152.000000      152.000000  152.000000
mean    95.516316   76.351579   60.627829  10622.703947       10.019737    8.539211
std      6.512357    8.990834    9.387800   2427.831793        5.862102    1.260299
min     71.030000   49.680000   29.460000   4700.000000        0.100000    3.720000
25%     95.807500   73.530000   58.445000   9164.250000        5.450000    7.952500
50%     97.985000   78.630000   61.420000  10678.000000        9.150000    8.635000
75%     98.660000   82.075000   65.960000  11698.000000       13.100000    9.272500
max     99.590000   88.210000   76.370000  19373.000000       28.700000   11.450000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                  APM_SD   APM_SMP   APM_SMA       PPK  PSN (Stunting)       RLS
APM_SD          1.000000  0.865300  0.814589  0.601733       -0.029268  0.719276
APM_SMP         0.865300  1.000000  0.892279  0.681253       -0.195576  0.737293
APM_SMA         0.814589  0.892279  1.000000  0.550540       -0.098321  0.764911
PPK             0.601733  0.681253  0.550540  1.000000       -0.380187  0.701371
PSN (Stunting) -0.029268 -0.195576 -0.098321 -0.380187        1.000000 -0.208481
RLS             0.719276  0.737293  0.764911  0.701371       -0.208481  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7885 
  *(Interpretasi: 78.85% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.4921 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.0515 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SD** diprediksi akan **naik** sebesar 0.0001 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SD** diprediksi akan **naik** sebesar 0.1800 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SD** diprediksi akan **naik** sebesar 0.8481 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8870 
  *(Interpretasi: 88.70% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.5012 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.5404 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMP** diprediksi akan **naik** sebesar 0.0008 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMP** diprediksi akan **turun** sebesar 0.1166 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMP** diprediksi akan **turun** sebesar 0.8107 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8479 
  *(Interpretasi: 84.79% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.0770 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.7927 unit.
- Setiap kenaikan 1 unit pada **PPK**, **APM_SMA** diprediksi akan **turun** sebesar 0.0008 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMA** diprediksi akan **naik** sebesar 0.0626 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMA** diprediksi akan **naik** sebesar 2.3990 unit.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.6430 
  *(Interpretasi: 64.30% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PPK** diprediksi akan **naik** sebesar 27.9906 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PPK** diprediksi akan **naik** sebesar 173.0823 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PPK** diprediksi akan **turun** sebesar 127.3666 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **PPK** diprediksi akan **turun** sebesar 80.5670 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PPK** diprediksi akan **naik** sebesar 984.2830 unit.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.2431 
  *(Interpretasi: 24.31% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.5219 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.3318 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.1215 unit.
- Setiap kenaikan 1 unit pada **PPK**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.0010 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.5109 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.7119 
  *(Interpretasi: 71.19% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **RLS** diprediksi akan **naik** sebesar 0.0433 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **RLS** diprediksi akan **turun** sebesar 0.0406 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **RLS** diprediksi akan **naik** sebesar 0.0819 unit.
- Setiap kenaikan 1 unit pada **PPK**, **RLS** diprediksi akan **naik** sebesar 0.0002 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **RLS** diprediksi akan **turun** sebesar 0.0090 unit.

