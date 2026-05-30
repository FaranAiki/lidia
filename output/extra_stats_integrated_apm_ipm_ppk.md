# Analisis Statistik Lanjutan: integrated_apm_ipm_ppk.csv

## 1. Hubungan antar Variabel (Korelasi Pearson)
Menunjukkan seberapa kuat hubungan antar indikator (1.0 = Sangat Kuat, 0 = Tidak Ada).

```
                 APM_SD   APM_SMP   APM_SMA  IPM_Laki_Laki  IPM_Perempuan       PPK
APM_SD         1.000000  0.870730  0.855871       0.853901       0.820953  0.613113
APM_SMP        0.870730  1.000000  0.917955       0.856658       0.882136  0.700294
APM_SMA        0.855871  0.917955  1.000000       0.821249       0.856651  0.663433
IPM_Laki_Laki  0.853901  0.856658  0.821249       1.000000       0.929397  0.844164
IPM_Perempuan  0.820953  0.882136  0.856651       0.929397       1.000000  0.852523
PPK            0.613113  0.700294  0.663433       0.844164       0.852523  1.000000
```

## 2. Analisis Ketimpangan Gender (Paired T-Test)
- **T-Statistic:** 16.0352
- **p-value:** 3.0640e-18
  - **Kesimpulan:** Ada perbedaan signifikan (Gender Gap) sebesar 6.60 poin antara Laki-laki dan Perempuan.


## 3. Ringkasan Statistik (Deskriptif)
```
          APM_SD    APM_SMP    APM_SMA  IPM_Laki_Laki  IPM_Perempuan           PPK
count  38.000000  38.000000  38.000000      38.000000      38.000000     38.000000
mean   95.092105  77.339737  64.423947      78.008947      71.412632  11962.473684
std     5.490588   7.456689   9.014287       4.665866       6.197836   2543.098384
min    72.550000  54.330000  35.590000      59.650000      52.390000   5861.000000
25%    95.675000  75.070000  61.525000      77.102500      69.697500  10598.250000
50%    96.390000  78.470000  65.610000      78.605000      72.140000  11977.500000
75%    97.547500  81.467500  70.245000      79.880000      74.237500  12766.250000
max    98.770000  88.670000  78.420000      86.840000      84.170000  20676.000000
```
