# Proyek Integrasi Data Sosio-Ekonomi (LIDIA)

## Deskripsi Proyek
Proyek ini bertujuan untuk mengintegrasikan berbagai indikator pembangunan manusia, pendidikan, ekonomi, dan kesehatan di Indonesia tingkat provinsi. Proyek ini mencakup proses ETL (Extract, Transform, Load) dari dataset mentah hingga analisis statistik tingkat lanjut untuk menghasilkan rekomendasi kebijakan berbasis data.

## Perbedaan Indikator Pendidikan (APM vs RLS)
Penting untuk membedakan dua indikator utama yang digunakan dalam proyek ini:
* **Angka Partisipasi Murni (APM)**: Mengukur persentase anak pada kelompok usia tertentu yang sedang sekolah di jenjang yang sesuai. Ini adalah indikator akses pendidikan saat ini.
* **Rata-rata Lama Sekolah (RLS)**: Mengukur jumlah tahun rata-rata yang telah dihabiskan penduduk (usia 25+) dalam pendidikan formal. Ini adalah indikator akumulasi kualitas modal manusia.

## Indikator Utama
Dataset ini mengintegrasikan lima dimensi utama:
1. Angka Partisipasi Murni (APM): Mencakup jenjang SD, SMP, dan SMA.
2. Indeks Pembangunan Manusia (IPM): Berdasarkan jenis kelamin (Laki-laki dan Perempuan) tahun 2025.
3. Pengeluaran Per Kapita (PPK): Ukuran kemampuan ekonomi masyarakat.
4. Prevalensi Stunting (PSN): Indikator kesehatan dan gizi anak.
5. Rata-rata Lama Sekolah (RLS): Durasi rata-rata pendidikan yang ditempuh penduduk.

## Struktur Direktori
* **dataset/**: Berisi file CSV mentah dan file hasil integrasi (integrated.csv, integrated_filled.csv).
* **partial_dataset/**: Berisi kombinasi dataset yang hanya menyertakan baris tanpa missing value untuk analisis spesifik.
* **script/**: Skrip Python untuk pemrosesan data, integrasi, dan analisis.
* **output/**: Laporan hasil analisis otomatis dalam format Markdown.

## Metodologi Analisis
Setiap dataset dianalisis melalui empat tahapan utama:

1. **Analisis Deskriptif**: Memberikan ringkasan statistik (mean, median, standar deviasi) untuk memahami distribusi dan jangkauan data pada setiap indikator.
2. **Analisis Diagnostik**: Menggunakan matriks korelasi Pearson untuk mengidentifikasi hubungan dan pola ketergantungan antar variabel.
3. **Analisis Prediktif**: Menggunakan Regresi Linier Berganda untuk melihat sejauh mana sebuah indikator dapat diprediksi oleh indikator lainnya (R-Squared).
4. **Analisis Preskriptif**: Menginterpretasikan koefisien regresi menjadi bobot aksi untuk memberikan rekomendasi variabel mana yang perlu diintervensi guna mengoptimalkan target tertentu.

## Cara Penggunaan

1. **Persiapan Data**:
   Pastikan semua data mentah tersedia di folder dataset/.

2. **Integrasi Data**:
   Jalankan skrip untuk menggabungkan semua data menjadi satu format long-form:
   python3 script/create_integrated_long.py

3. **Pembuatan Dataset Parsial**:
   Guna menghindari bias akibat missing value yang terlalu banyak pada tahun-tahun tertentu, buat dataset kombinasi otomatis:
   python3 script/create_partial_datasets.py

4. **Menjalankan Analisis**:
   Hasilkan laporan analisis untuk setiap kombinasi dataset:
   python3 script/analysis.py

Hasil analisis dapat dilihat di folder output/ dalam format .md.

## Persyaratan Sistem
* Python 3.x
* Pandas
* Numpy

## Catatan Penting
Analisis yang melibatkan IPM (2025) memiliki keterbatasan jumlah baris karena data IPM dalam dataset ini bersifat cross-sectional (hanya satu tahun). Perbedaan tren antara APM dan IPM pada beberapa laporan mungkin disebabkan oleh heterogenitas karakteristik wilayah atau keterbatasan jumlah sampel data pada tahun terkait.
