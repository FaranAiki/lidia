# Analysis Report: integrated_apm_rls

## 1. Descriptive Analysis
Descriptive statistics summarize the central tendency, dispersion, and shape of the dataset's distribution.

           APM_SD     APM_SMP     APM_SMA         RLS
count  570.000000  570.000000  570.000000  570.000000
mean    94.048544   72.512298   56.664035    8.037351
std      6.867018   10.378228   11.321300    1.364327
min     68.000000   40.390000   17.200000    2.480000
25%     93.037500   68.237500   51.712500    7.370000
50%     96.480000   74.940000   59.330000    8.110000
75%     98.087500   79.767500   63.867500    8.870000
max     99.590000   90.140000   77.860000   11.490000

## 2. Diagnostic Analysis
Diagnostic analysis explores the relationships between variables using a Pearson correlation matrix. Values closer to 1 or -1 indicate strong relationships.

           APM_SD   APM_SMP   APM_SMA       RLS
APM_SD   1.000000  0.848609  0.801108  0.721262
APM_SMP  0.848609  1.000000  0.915163  0.748639
APM_SMA  0.801108  0.915163  1.000000  0.778190
RLS      0.721262  0.748639  0.778190  1.000000

## 3. Predictive & 4. Prescriptive Analysis
Using Multiple Linear Regression to understand how each variable can be predicted and influenced by the others.

### Target: APM_SD
**Predictive (Model Fit):**
- **R-squared**: 0.7372 
  *(Interpretasi: 73.72% varians dari APM_SD dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SD, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SD** diprediksi akan **naik** sebesar 0.4426 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SD** diprediksi akan **naik** sebesar 0.0267 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SD** diprediksi akan **naik** sebesar 0.9374 unit.

### Target: APM_SMP
**Predictive (Model Fit):**
- **R-squared**: 0.8748 
  *(Interpretasi: 87.48% varians dari APM_SMP dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMP, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMP** diprediksi akan **naik** sebesar 0.4816 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **APM_SMP** diprediksi akan **naik** sebesar 0.5953 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMP** diprediksi akan **naik** sebesar 0.1020 unit.

### Target: APM_SMA
**Predictive (Model Fit):**
- **R-squared**: 0.8574 
  *(Interpretasi: 85.74% varians dari APM_SMA dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) APM_SMA, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **APM_SMA** diprediksi akan **naik** sebesar 0.0394 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **APM_SMA** diprediksi akan **naik** sebesar 0.8071 unit.
- Setiap kenaikan 1 unit pada **RLS**, **APM_SMA** diprediksi akan **naik** sebesar 1.7181 unit.

### Target: RLS
**Predictive (Model Fit):**
- **R-squared**: 0.6325 
  *(Interpretasi: 63.25% varians dari RLS dapat diprediksi/dijelaskan oleh variabel lainnya di model ini)*

**Prescriptive (Actionable Insights):**
Untuk mengoptimalkan (menaikkan/menurunkan) RLS, perhatikan bobot (koefisien) variabel berikut (berdasarkan model linier):
- Setiap kenaikan 1 unit pada **APM_SD**, **RLS** diprediksi akan **naik** sebesar 0.0517 unit.
- Setiap kenaikan 1 unit pada **APM_SMP**, **RLS** diprediksi akan **naik** sebesar 0.0052 unit.
- Setiap kenaikan 1 unit pada **APM_SMA**, **RLS** diprediksi akan **naik** sebesar 0.0643 unit.

