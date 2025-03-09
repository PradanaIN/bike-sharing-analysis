# README: Dashboard Analisis Data Bike Sharing

## 📌 Deskripsi Proyek

Proyek ini adalah dashboard interaktif berbasis Streamlit yang menampilkan hasil analisis data peminjaman sepeda. Dashboard ini mencakup berbagai visualisasi untuk memahami pola penggunaan sepeda berdasarkan musim, cuaca, hari kerja, serta kategori permintaan berdasarkan clustering.

## 🛠️ Instalasi dan Persiapan

Sebelum menjalankan proyek ini, pastikan Anda memiliki Python terinstal di sistem Anda. Ikuti langkah-langkah berikut untuk mengatur lingkungan proyek:

### 1️⃣ Clone Repository (Opsional)

Jika proyek ini berada di dalam repositori Git, Anda bisa mengkloningnya dengan perintah berikut:

```bash
git clone https://github.com/PradanaIN/bike-sharing-analysis.git
cd repository
```

### 2️⃣ Buat Virtual Environment (Opsional)

Disarankan menggunakan virtual environment agar dependensi proyek tidak bentrok dengan sistem lain.

```bash
python -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
venv\Scripts\activate    # Untuk Windows
```

### 3️⃣ Instal Dependensi

Jalankan perintah berikut untuk menginstal semua pustaka yang dibutuhkan:

```bash
pip install -r requirements.txt
```

Jika tidak ada file `requirements.txt`, Anda bisa menginstal pustaka secara manual:

```bash
pip install streamlit pandas matplotlib seaborn plotly
```

## 🚀 Menjalankan Dashboard

Setelah instalasi selesai, jalankan perintah berikut untuk membuka dashboard:

```bash
streamlit run dashboard.py
```

Tunggu beberapa saat hingga browser terbuka secara otomatis dengan tampilan dashboard.

## 🎯 Fitur Dashboard

Berikut adalah fitur utama dalam dashboard ini:

### 1️⃣ **Distribusi Peminjaman Sepeda**

- Menampilkan sebaran jumlah peminjaman sepeda dalam bentuk histogram atau boxplot.
- Memudahkan dalam melihat tren peminjaman berdasarkan musim dan bulan.

### 2️⃣ **Pengaruh Musim dan Cuaca terhadap Peminjaman**

- Menampilkan jumlah peminjaman sepeda berdasarkan musim dan kondisi cuaca.
- Memvisualisasikan pola penggunaan sepeda pada hari kerja dan akhir pekan.

### 3️⃣ **Pola Peminjaman Sepeda Berdasarkan Jam**

- Menunjukkan jam-jam dengan tingkat peminjaman tertinggi dan terendah dalam sehari.
- Memvisualisasikan tren peminjaman di hari kerja vs akhir pekan.

### 4️⃣ **Clustering Kategori Permintaan Sepeda**

- Mengelompokkan jumlah peminjaman menjadi kategori permintaan rendah, sedang, dan tinggi.
- Memudahkan dalam melihat pola permintaan berdasarkan berbagai faktor seperti musim, cuaca, dan waktu.

## 🔧 Troubleshooting

Jika terjadi error saat menjalankan Streamlit, coba langkah berikut:

1. Pastikan semua pustaka telah diinstal dengan benar.
2. Jalankan ulang perintah `streamlit run dashboard.py` dari direktori proyek.
3. Jika masih mengalami kendala, perbarui pustaka dengan:
   ```bash
   pip install --upgrade streamlit pandas matplotlib seaborn plotly
   ```
4. Pastikan Anda berada dalam virtual environment (jika digunakan).

## 📩 Kontak & Kontribusi

Jika Anda memiliki saran, pertanyaan, atau ingin berkontribusi dalam proyek ini, silakan hubungi atau buat pull request di repositori GitHub ini.

---

🚀 **Selamat Menganalisis!** 🚲📊
