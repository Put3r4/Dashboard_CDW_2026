"""Konfigurasi global palet warna, direktori, dan konstanta aplikasi."""

from pathlib import Path

# Direktori Proyek (berjalan konsisten lokal maupun cloud tanpa path absolut / backslash manual)
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data_set"

# File Sumber Dataset
DATA_FILES = {
    "profil": DATA_DIR / "1_profil_mahasiswa_umum.csv",
    "prestasi": DATA_DIR / "2_prestasi_mahasiswa.csv",
    "gen1": DATA_DIR / "3_generasi_pertama_kuliah.csv",
    "sosek": DATA_DIR / "4_status_sosial_ekonomi.csv",
    "ipk": DATA_DIR / "5_riwayat_ipk_semester.csv",
    "kamus_data": DATA_DIR / "Kamus Data Infographic Competition.pdf",
}

# Palet Warna Resmi CDW 2026
COLOR_BG = "#f1faee"           # Latar halaman
COLOR_CARD = "#ffffff"         # Latar kartu
COLOR_TEXT = "#1d3557"         # Teks utama, judul, sidebar
COLOR_PRIMARY = "#457b9d"      # Warna utama grafik dan tombol
COLOR_SECONDARY = "#a8dadc"    # Warna sekunder, grid, latar pil
COLOR_ACCENT = "#e63946"       # Sorotan (Gen 1, kesenjangan, peringatan)

# Pemetaan Warna Data Konsisten
COLOR_GEN1 = COLOR_ACCENT      # #e63946
COLOR_NON_GEN1 = COLOR_PRIMARY # #457b9d

COLOR_MENTORED = COLOR_TEXT     # #1d3557
COLOR_NON_MENTORED = COLOR_SECONDARY  # #a8dadc

# Palet Status Pil Uji Ketahanan
STATUS_COLORS = {
    "Bertahan": {"bg": "#d1fae5", "text": "#065f46", "border": "#a7f3d0"},
    "Kuat": {"bg": "#d1fae5", "text": "#065f46", "border": "#a7f3d0"},
    "Melemah": {"bg": "#fef3c7", "text": "#92400e", "border": "#fde68a"},
    "Terbatas": {"bg": "#fef3c7", "text": "#92400e", "border": "#fde68a"},
    "Gugur": {"bg": "#fee2e2", "text": "#991b1b", "border": "#fecaca"},
    "Batas Temuan": {"bg": "#e0f2fe", "text": "#075985", "border": "#bae6fd"},
}

# Informasi Metadata Aplikasi
APP_TITLE = "Dashboard CDW 2026"
CAMPUS_NAME = "Universitas X"
THEME_TITLE = "Meretas Ketimpangan, Mengukir Prestasi: Peran Ekosistem Pendampingan Mahasiswa Generasi Pertama"
DATA_TYPE_DISCLAIMER = "Data Fiktif Real World Fake Data (RWFD) - Sensus Penuh N = 5.000 Mahasiswa"
CONTROL_LABEL_HERO = "Setelah menyamakan IP semester 1, angkatan, masa studi, fakultas, kondisi ekonomi, beasiswa, dan tempat tinggal"
