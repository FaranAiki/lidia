# Analysis Report: integrated_ppk_psn_rls

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

                PPK  PSN (Stunting)         RLS
count    152.000000      152.000000  152.000000
mean   10622.703947       10.019737    8.539211
std     2427.831793        5.862102    1.260299
min     4700.000000        0.100000    3.720000
25%     9164.250000        5.450000    7.952500
50%    10678.000000        9.150000    8.635000
75%    11698.000000       13.100000    9.272500
max    19373.000000       28.700000   11.450000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                     PPK  PSN (Stunting)       RLS
PPK             1.000000       -0.380187  0.701371
PSN (Stunting) -0.380187        1.000000 -0.208481
RLS             0.701371       -0.208481  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.5491 
  *(Interpretasi: 54.91% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **PPK** diprediksi akan **turun** sebesar 101.3013 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PPK** diprediksi akan **naik** sebesar 1252.8821 unit.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.1512 
  *(Interpretasi: 15.12% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **PPK**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.0011 unit.
- Setiap kenaikan 1 unit pada **RLS**, **PSN (Stunting)** diprediksi akan **naik** sebesar 0.5325 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.4959 
  *(Interpretasi: 49.59% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **PPK**, **RLS** diprediksi akan **naik** sebesar 0.0004 unit.
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **RLS** diprediksi akan **naik** sebesar 0.0146 unit.

