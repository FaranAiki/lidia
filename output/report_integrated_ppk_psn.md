# Analysis Report: integrated_ppk_psn

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

                PPK  PSN (Stunting)
count    152.000000      152.000000
mean   10622.703947       10.019737
std     2427.831793        5.862102
min     4700.000000        0.100000
25%     9164.250000        5.450000
50%    10678.000000        9.150000
75%    11698.000000       13.100000
max    19373.000000       28.700000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                     PPK  PSN (Stunting)
PPK             1.000000       -0.380187
PSN (Stunting) -0.380187        1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: PPK
**Predictive (Model Fit):**
- **R-squared**: 0.1445 
  *(Interpretasi: 14.45% varians dari PPK dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PPK, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **PPK** diprediksi akan **turun** sebesar 157.4573 unit.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.1445 
  *(Interpretasi: 14.45% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **PPK**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.0009 unit.

