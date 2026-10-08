# Dashboard Streamlit CDW 2026

Dashboard Pendamping Infografis A3 - Campus Data Week (CDW) 2026  
Tema: "Meretas Ketimpangan, Mengukir Prestasi: Peran Ekosistem Pendampingan Mahasiswa Generasi Pertama"  
Institusi: Universitas X (Dataset Real World Fake Data / RWFD, Sensus Penuh N = 5.000 Mahasiswa)

---

## 1. Deskripsi Proyek

Repositori ini memuat aplikasi dashboard interaktif berbasis Streamlit yang dirancang sebagai pendamping resmi poster infografis cetak A3 tim kami dalam kompetisi Campus Data Week (CDW) 2026. Pengunjung dan dewan juri mengakses dashboard ini dengan memindai QR Code pada poster melalui ponsel atau peramban desktop.

Pesan Utama dalam Tiga Menit:
1. Mahasiswa generasi pertama (Gen 1) mencakup 38,48% populasi kampus (1.924 mahasiswa) dan menanggung beban ganda finansial serta adaptasi 1,48 kali lipat lebih tinggi dibanding rekan non-generasi pertama.
2. Program pendampingan berasosiasi dengan nilai tambah akademik bersih sebesar +0,0737 poin IPK (p = 2,02 x 10^-14, 95% CI [0,0548; 0,0926]) setelah mengontrol nilai awal, angkatan, masa studi, fakultas, kondisi ekonomi, beasiswa, dan tempat tinggal.
3. Kesenjangan akademik di tingkat universitas belum tertutup: mahasiswa generasi pertama yang didampingi (IPK 3,01) masih tertinggal 0,33 poin dari mahasiswa non-generasi pertama (IPK 3,33).

---

## 2. Struktur Direktori Proyek

```
Dashboard_CDW_2026/
├── app.py                    # Titik masuk utama aplikasi, navigasi, dan konfigurasi global
├── pages/
│   ├── 1_Selamat_Datang.py   # Pengenalan tema, hook, ringkasan 5 tabel, dan panduan membaca
│   ├── 2_Overview.py         # Metrik KPI kampus, sebaran demografi, dan pertanyaan pemantik
│   ├── 3_Kendala.py          # Analisis beban finansial, adaptasi, dukungan, dan kesenjangan
│   ├── 4_Insight.py          # Hero metric terkontrol, IPW, panel semester 8, dan evaluasi klaim
│   ├── 5_Kesimpulan.py       # Tiga temuan inti, angka sorotan, dan rekomendasi kebijakan
│   └── 6_Reference.py        # Spesifikasi teknis, pipeline notebook, kode model, dan audit V1-V12
├── utils/
│   ├── config.py             # Palet warna resmi, direktori, dan konstanta aplikasi
│   ├── data_loader.py        # Ingestion data, validasi jumlah baris, dan feature engineering
│   ├── charts.py             # Fungsi grafik visual Plotly bertema SaaS seragam
│   ├── components.py         # Kartu KPI, kartu hero metric, pil status, dan layout CSS
│   └── results.py            # Konstanta angka inferensial tervalidasi (V1 s.d. V12)
├── content.py                # Seluruh draf teks narasi terstruktur dengan penanda tim
├── check_numbers.py          # Skrip audit pencocokan angka deskriptif vs data mentah Tier A
├── .streamlit/
│   └── config.toml           # Konfigurasi tema visual Streamlit
├── data_set/                 # 5 berkas CSV resmi dan Kamus Data PDF
├── requirements.txt          # Daftar dependensi paket produksi Python
├── .gitignore                # Berkas pengabaian git standar Python
└── README.md                 # Dokumentasi panduan operasional proyek
```

---

## 3. Cara Menjalankan Aplikasi Secara Lokal

### Prasyarat
- Python versi 3.10 ke atas (diuji pada Python 3.12)
- Pengelola paket `pip`

### Langkah Instalasi dan Eksekusi
1. Buka terminal atau PowerShell pada direktori proyek `Dashboard_CDW_2026`.
2. Buat dan aktifkan lingkungan virtual (disarankan):
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - Linux / macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Pasang seluruh pustaka yang dipersyaratkan:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan audit pencocokan angka untuk memastikan integritas data:
   ```bash
   python check_numbers.py
   ```
5. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run app.py
   ```
6. Buka peramban di alamat `http://localhost:8501`.

---

## 4. Panduan Deployment ke Streamlit Community Cloud

Aplikasi ini telah dirancang untuk siap dipublikasikan secara langsung ke Streamlit Community Cloud:

1. Buat repositori publik baru di GitHub (misalnya: `Dashboard_CDW_2026`).
2. Unggah seluruh isi folder proyek beserta folder `data_set/` ke repositori GitHub tersebut. Pastikan folder `data_set/` disertakan agar aplikasi cloud dapat membaca data secara otomatis.
3. Masuk ke laman [share.streamlit.io](https://share.streamlit.io/) menggunakan akun GitHub.
4. Klik **New app**, pilih repositori yang telah dibuat, tentukan branch utama (`main` atau `master`), dan atur file jalur utama ke `app.py`.
5. Klik **Deploy!**. Aplikasi akan membangun lingkungan dan aktif dalam waktu kurang dari dua menit.
6. Pastikan pengaturan visibilitas aplikasi diatur menjadi **Public** agar siapa pun yang memindai QR Code dapat membukanya tanpa perlu masuk log.

---

## 5. Saran Implementasi QR Code pada Poster A3

- Gunakan tautan URL final yang stabil dan permanen dari Streamlit Community Cloud (misalnya format kustom atau shortlink resmi).
- Cetak QR Code pada kuadran kanan bawah poster infografis A3 dengan ukuran minimal 3 x 3 cm (disarankan 3,5 x 3,5 cm) untuk memastikan keterbacaan pemindaian optimal pada resolusi cetak 300 DPI.
- Berikan label teks pendamping di bawah QR Code: *"Pindai untuk eksplorasi data interaktif dan audit metodologi lengkap"*.
- Lakukan uji pemindaian menggunakan beberapa tipe kamera ponsel pintar sebelum mencetak versi final.

---

## 6. Catatan Etika & Sifat Data

- **Real World Fake Data (RWFD):** Seluruh data merupakan data sintetis simulasi institusi yang disiapkan oleh panitia Campus Data Week 2026 untuk menguji kemampuan analitik dan penceritaan data.
- **Anonimitas Kampus:** Sesuai ketentuan, nama universitas disamarkan sebagai Universitas X.
- **Sifat Observasional:** Data bersifat observasional. Hubungan antarvariabel yang disajikan merupakan pola asosiasi empiris terkontrol, bukan pembuktian kausalitas langsung.
