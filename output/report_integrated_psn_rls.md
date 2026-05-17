# Analysis Report: integrated_psn_rls

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

       PSN (Stunting)         RLS
count      152.000000  152.000000
mean        10.019737    8.539211
std          5.862102    1.260299
min          0.100000    3.720000
25%          5.450000    7.952500
50%          9.150000    8.635000
75%         13.100000    9.272500
max         28.700000   11.450000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

                PSN (Stunting)       RLS
PSN (Stunting)        1.000000 -0.208481
RLS                  -0.208481  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: PSN (Stunting)
**Predictive (Model Fit):**
- **R-squared**: 0.0435 
  *(Interpretasi: 4.35% varians dari PSN (Stunting) dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) PSN (Stunting), perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **RLS**, **PSN (Stunting)** diprediksi akan **turun** sebesar 0.9697 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.0435 
  *(Interpretasi: 4.35% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **PSN (Stunting)**, **RLS** diprediksi akan **turun** sebesar 0.0448 unit.

