# Analysis Report: integrated_apm_psn_rls

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA  PSN (Stunting)         RLS
count  152.000000  152.000000  152.000000      152.000000  152.000000
mean    95.516316   76.351579   60.627829       10.019737    8.539211
std      6.512357    8.990834    9.387800        5.862102    1.260299
min     71.030000   49.680000   29.460000        0.100000    3.720000
25%     95.807500   73.530000   58.445000        5.450000    7.952500
50%     97.985000   78.630000   61.420000        9.150000    8.635000
75%     98.660000   82.075000   65.960000       13.100000    9.272500
max     99.590000   88.210000   76.370000       28.700000   11.450000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                  APM_SD   APM_SMP   APM_SMA  PSN (Stunting)       RLS
APM_SD          1.000000  0.865300  0.814589       -0.029268  0.719276
APM_SMP         0.865300  1.000000  0.892279       -0.195576  0.737293
APM_SMA         0.814589  0.892279  1.000000       -0.098321  0.764911
PSN (Stunting) -0.029268 -0.195576 -0.098321        1.000000 -0.208481
RLS             0.719276  0.737293  0.764911       -0.208481  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7878 
  *(Interpretasi: 78.78% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.5145 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.0364 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SD** diprediksi akan **naik** sebesar 0.1710 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SD** diprediksi akan **naik** sebesar 0.9688 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8701 
  *(Interpretasi: 87.01% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.6004 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.5112 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMP** diprediksi akan **turun** sebesar 0.2036 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMP** diprediksi akan **turun** sebesar 0.0815 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8304 
  *(Interpretasi: 83.04% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.0605 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.7275 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **APM_SMA** diprediksi akan **naik** sebesar 0.1427 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMA** diprediksi akan **naik** sebesar 1.7848 unit.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.1771 
  *(Interpretasi: 17.71% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.5371 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.5482 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.2700 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PSN (Stunting)** diprediksi akan **turun** sebesar 1.6212 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.6350 
  *(Interpretasi: 63.50% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **RLS** diprediksi akan **naik** sebesar 0.0624 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **RLS** diprediksi akan **turun** sebesar 0.0045 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **RLS** diprediksi akan **naik** sebesar 0.0692 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **RLS** diprediksi akan **turun** sebesar 0.0332 unit.

