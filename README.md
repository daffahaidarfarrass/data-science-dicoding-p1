# 🚲 Proyek Analisis Data: Bike-sharing Dataset

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis pola penggunaan layanan penyewaan sepeda berdasarkan data historis dari tahun **2011 hingga 2012**. Fokus analisis diarahkan pada **pertumbuhan transaksi dan pengguna baru**, serta **performa rental sepeda berdasarkan musim dan jam penggunaan**.

---

## 👤 Informasi Kontributor

- **Nama**: Daffa Haidar Farras  
- **Email**: daffahaidarfarras@gmail.com  
- **ID Dicoding**: daffa_haidar  

---

## 🎯 Pertanyaan Bisnis

1. Bagaimana pertumbuhan transaksi rental sepeda dan pengguna baru dari tahun 2011 hingga 2012?
2. Bagaimana performa rental sepeda berdasarkan **musim** dan **jam**?

---

## 📊 Insight & Visualisasi

### 🔹 Pertanyaan 1: Pertumbuhan Transaksi dan Pengguna Baru

- **Line Plot** digunakan untuk menunjukkan pertumbuhan:
  - **Transaksi Rental Sepeda** berdasarkan kolom `cnt` (total transaksi per hari) yang digabungkan menjadi bulanan.
  - **Pengguna Baru** berdasarkan kolom `registered` (pengguna terdaftar baru per hari), juga dalam agregasi bulanan.
- **Insight**:
  - Terlihat adanya **tren naik** dari 2011 ke 2012, baik untuk transaksi maupun pengguna baru.
  - Korelasi positif antara peningkatan pengguna baru dengan peningkatan transaksi.
  - 📌 **Rekomendasi**: Lakukan promosi aktif untuk menarik lebih banyak pengguna baru demi meningkatkan transaksi.

### 🔹 Pertanyaan 2: Performa Berdasarkan Musim dan Jam

- **Bar Plot** digunakan untuk menganalisis:
  - **Transaksi berdasarkan musim** (`season`), dikelompokkan per tahun.
  - **Transaksi berdasarkan jam** (`hr`), dikelompokkan per tahun.
- **Insight**:
  - Terjadi peningkatan transaksi dari 2011 ke 2012 di semua musim dan semua jam.
  - Namun, **musim gugur** menunjukkan jumlah transaksi yang lebih rendah dibanding musim lainnya.
  - 📌 **Rekomendasi**: Adakan event atau promosi khusus di musim gugur untuk mendorong peningkatan transaksi.

---

## 🧠 Kesimpulan

### ✅ Pertanyaan 1:
> Terdapat pertumbuhan signifikan dalam jumlah transaksi dan pengguna baru dari tahun 2011 ke 2012. Tindakan strategis seperti promosi pengguna baru berpotensi meningkatkan total transaksi penyewaan.

### ✅ Pertanyaan 2:
> Secara umum performa rental meningkat, namun musim gugur menunjukkan performa yang kurang optimal. Perlu adanya promosi musiman untuk menjaga keseimbangan jumlah transaksi sepanjang tahun.

---

## 🛠️ Tools dan Teknologi

- Python
- Pandas
- Matplotlib / Seaborn
- Jupyter Notebook
- (Optional) Streamlit atau Plotly untuk visualisasi interaktif
