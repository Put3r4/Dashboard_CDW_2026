"""Halaman 1: Selamat Datang - Gerbang Utama Dashboard CDW 2026.

Menyajikan judul tema, hook utama, perkenalan data Universitas X (RWFD N=5.000),
ringkasan 5 tabel dataset, kartu navigasi antarhalaman berpanah (→),
serta panduan membaca dashboard.
"""

from pathlib import Path
import streamlit as st

from utils.config import (
    APP_TITLE,
    CAMPUS_NAME,
    THEME_TITLE,
    CONTROL_LABEL_HERO,
    COLOR_PRIMARY,
    COLOR_ACCENT,
    COLOR_TEXT,
)
from utils.components import (
    apply_custom_css,
    render_sidebar_header,
    render_page_header,
    render_section_title,
    render_narrative_block,
    st_html,
)
from content import CONTENT

st.set_page_config(
    page_title=f"Selamat Datang - {APP_TITLE}",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_custom_css()
render_sidebar_header()

# Header Halaman
render_page_header(
    title=THEME_TITLE,
    subtitle=f"Dashboard Analisis Mahasiswa Generasi Pertama di {CAMPUS_NAME} - Campus Data Week (CDW) 2026",
)

# Hook Utama Terintegrasi
st_html(
    f"""
    <div style="background: #ffffff; border-left: 5px solid {COLOR_ACCENT}; border-radius: 0 14px 14px 0; padding: 22px 26px; box-shadow: 0 2px 12px rgba(29,53,87,0.07); margin-bottom: 24px;">
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: {COLOR_ACCENT}; margin-bottom: 6px;">
            PESAN KUNCI PROYEK
        </div>
        <div style="font-size: 17px; font-weight: 600; color: {COLOR_TEXT}; line-height: 1.55;">
            {CONTENT['selamat_datang']['hook']['teks']}
        </div>
        <div style="font-size: 12.5px; color: #64748b; margin-top: 10px; border-top: 1px solid rgba(168,218,220,0.35); padding-top: 8px;">
            <strong>Fakta Inti:</strong> {' • '.join(CONTENT['selamat_datang']['hook']['poin_data'])}
        </div>
    </div>
    """
)

# Perkenalan Data Universitas X
render_section_title("Perkenalan Data Institusional")
render_narrative_block(CONTENT["selamat_datang"]["perkenalan_data"])

# Ringkasan 5 Tabel Data
render_section_title("Struktur Lima Tabel Dataset Resmi")

col1, col2, col3 = st.columns(3)
with col1:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 11.5px; font-weight: 700; color: #457b9d; margin-bottom: 4px;">TABEL 1 - DEMOGRAFI</div>
            <div style="font-size: 16px; font-weight: 700; color: #1d3557; margin-bottom: 4px;">Profil Mahasiswa Umum</div>
            <div style="font-size: 13px; color: #e63946; font-weight: 600; margin-bottom: 8px;">5.000 Baris</div>
            <div style="font-size: 13px; color: #475569; line-height: 1.45;">
                Karakteristik demografi mahasiswa, jenis kelamin, usia, fakultas, program studi, angkatan, IPK akhir, dan masa studi.
            </div>
        </div>
        """
    )

with col2:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 11.5px; font-weight: 700; color: #457b9d; margin-bottom: 4px;">TABEL 2 - PRESTASI</div>
            <div style="font-size: 16px; font-weight: 700; color: #1d3557; margin-bottom: 4px;">Prestasi Mahasiswa</div>
            <div style="font-size: 13px; color: #e63946; font-weight: 600; margin-bottom: 8px;">6.414 Baris</div>
            <div style="font-size: 13px; color: #475569; line-height: 1.45;">
                Log seluruh rekaman kegiatan kompetisi kampus, bidang kegiatan, tingkat kegiatan, capaian prestasi, dan tahun perolehan.
            </div>
        </div>
        """
    )

with col3:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 11.5px; font-weight: 700; color: #457b9d; margin-bottom: 4px;">TABEL 3 - LATAR BELAKANG</div>
            <div style="font-size: 16px; font-weight: 700; color: #1d3557; margin-bottom: 4px;">Generasi Pertama Kuliah</div>
            <div style="font-size: 13px; color: #e63946; font-weight: 600; margin-bottom: 8px;">5.000 Baris</div>
            <div style="font-size: 13px; color: #475569; line-height: 1.45;">
                Status generasi pertama, pendidikan dan pekerjaan orang tua, skor dukungan keluarga, kendala utama, dan partisipasi pendampingan.
            </div>
        </div>
        """
    )

col4, col5 = st.columns(2)
with col4:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 11.5px; font-weight: 700; color: #457b9d; margin-bottom: 4px;">TABEL 4 - SOSIAL EKONOMI</div>
            <div style="font-size: 16px; font-weight: 700; color: #1d3557; margin-bottom: 4px;">Status Sosial Ekonomi</div>
            <div style="font-size: 13px; color: #e63946; font-weight: 600; margin-bottom: 8px;">5.000 Baris</div>
            <div style="font-size: 13px; color: #475569; line-height: 1.45;">
                Kategori ekonomi, rentang pendapatan orang tua, jumlah tanggungan, status dan jenis beasiswa, kategori UKT, serta status bekerja.
            </div>
        </div>
        """
    )

with col5:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 11.5px; font-weight: 700; color: #457b9d; margin-bottom: 4px;">TABEL 5 - RIWAYAT NILAI</div>
            <div style="font-size: 16px; font-weight: 700; color: #1d3557; margin-bottom: 4px;">Riwayat IPK Semester</div>
            <div style="font-size: 13px; color: #e63946; font-weight: 600; margin-bottom: 8px;">25.099 Baris</div>
            <div style="font-size: 13px; color: #475569; line-height: 1.45;">
                Rekaman longitudinal nilai Indeks Prestasi (IP) semester berjalan dan IPK kumulatif dari Semester 1 hingga Semester 8.
            </div>
        </div>
        """
    )

# Panduan Menelusuri Dashboard (Navigasi Antarhalaman)
render_section_title("Jelajahi Halaman Dashboard")

nav_pages = [
    {
        "title": "Overview",
        "file": "pages/2_Overview.py",
        "desc": "Gambaran umum skala demografi kampus, sebaran fakultas, angkatan, distribusi IPK, dan partisipasi kegiatan kompetisi.",
    },
    {
        "title": "Kendala",
        "file": "pages/3_Kendala.py",
        "desc": "Pemeriksaan beban finansial, beban ganda adaptasi, defisit dukungan keluarga, serta jurang kesenjangan IPK 0,35 poin.",
    },
    {
        "title": "Insight",
        "file": "pages/4_Insight.py",
        "desc": "Analisis inti nilai tambah terkontrol (+0,074 poin), penyeimbangan IPW, lintasan panel mahasiswa semester 8, dan batas temuan.",
    },
    {
        "title": "Kesimpulan",
        "file": "pages/5_Kesimpulan.py",
        "desc": "Rangkuman tiga temuan utama, angka sorotan kebijakan, dan rekomendasi struktural institusional bagi pimpinan kampus.",
    },
    {
        "title": "Reference",
        "file": "pages/6_Reference.py",
        "desc": "Dokumentasi pustaka, alur pipeline lima notebook, cuplikan kode model, dan ringkasan 12 uji ketahanan (V1 sampai V12).",
    },
]

for p in nav_pages:
    col_desc, col_btn = st.columns([4, 1.2])
    with col_desc:
        st_html(
            f"""
            <div style="padding: 10px 0;">
                <strong style="font-size: 15px; color: {COLOR_TEXT};">{p['title']}</strong>:
                <span style="font-size: 14px; color: #475569;"> {p['desc']}</span>
            </div>
            """
        )
    with col_btn:
        if st.button(f"Buka {p['title']} →", key=f"btn_nav_{p['title']}"):
            st.switch_page(p["file"])

# Kotak Cara Membaca Dashboard Ini
render_section_title("Cara Membaca Dashboard Ini")
render_narrative_block(CONTENT["selamat_datang"]["cara_membaca"])

st_html(
    """
    <div class="saas-card" style="background: #ffffff; border-left: 4px solid #457b9d; margin-top: 14px;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
            <div>
                <strong style="color: #1d3557; font-size: 13.5px;">1. Mahasiswa Generasi Pertama (Gen 1)</strong>
                <p style="font-size: 13px; color: #475569; margin-top: 4px; line-height: 1.45;">
                    Mahasiswa yang kedua orang tuanya tidak memiliki ijazah perguruan tinggi (maksimal tamat SMA/sederajat). Berjumlah 1.924 orang (38,48% populasi kampus).
                </p>
            </div>
            <div>
                <strong style="color: #1d3557; font-size: 13.5px;">2. Program Pendampingan</strong>
                <p style="font-size: 13px; color: #475569; margin-top: 4px; line-height: 1.45;">
                    Intervensi institusional kampus berupa bimbingan akademik, pendampingan belajar, dan adaptasi sosial bagi mahasiswa.
                </p>
            </div>
            <div>
                <strong style="color: #1d3557; font-size: 13.5px;">3. Nilai Tambah Terkontrol (Value-Added)</strong>
                <p style="font-size: 13px; color: #475569; margin-top: 4px; line-height: 1.45;">
                    Keunggulan nilai bersih yang dikaitkan dengan pendampingan setelah faktor pembanding (nilai awal, ekonomi, fakultas, beasiswa) disetarakan secara adil.
                </p>
            </div>
            <div>
                <strong style="color: #1d3557; font-size: 13.5px;">4. Bahasa Asosiasi</strong>
                <p style="font-size: 13px; color: #475569; margin-top: 4px; line-height: 1.45;">
                    Seluruh hubungan memakai bahasa asosiasi ("berasosiasi dengan", "dikaitkan dengan"), bukan sebab-akibat langsung, sesuai sifat data observasional.
                </p>
            </div>
        </div>
    </div>
    """
)
