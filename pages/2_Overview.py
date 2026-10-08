"""Halaman 2: Overview - Lanskap Demografi & Akademik Kampus.

Menyajikan metrik KPI universitas, grafik sebaran fakultas, angkatan, distribusi IPK,
komposisi Gen 1 vs Non-Gen 1, kegiatan kompetisi per tingkat,
serta bagian pemantik "Pertanyaan yang Masih Kami Cari Jawabannya" berpanah ke Kendala/Insight.
Mendukung filter interaktif fakultas dan angkatan di sidebar.
"""

import streamlit as st
import pandas as pd

from utils.config import (
    APP_TITLE,
    CAMPUS_NAME,
    COLOR_PRIMARY,
    COLOR_ACCENT,
    COLOR_TEXT,
)
from utils.components import (
    apply_custom_css,
    render_sidebar_header,
    render_page_header,
    render_section_title,
    render_kpi_card,
    render_narrative_block,
    st_html,
    clean_html,
)
from utils.data_loader import get_data, filter_data
from utils.charts import (
    chart_komposisi_gen1,
    chart_sebaran_angkatan,
    chart_sebaran_fakultas,
    chart_distribusi_ipk,
    chart_prestasi_per_tingkat,
)
from content import CONTENT

st.set_page_config(
    page_title=f"Overview - {APP_TITLE}",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_custom_css()
render_sidebar_header()

# Pemuatan data
df_master, df_ipk, df_prestasi = get_data()

# Filter Sidebar untuk Deskriptif
st.sidebar.markdown(
    clean_html(
        """
        <div style="font-size: 13px; font-weight: 700; color: #f1faee; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 10px; margin-bottom: 8px;">
            Filter Deskriptif
        </div>
        """
    ),
    unsafe_allow_html=True,
)

fakultas_list = ["Semua Fakultas"] + sorted(df_master["Fakultas"].dropna().unique().tolist())
selected_fakultas = st.sidebar.selectbox("Fakultas", fakultas_list, index=0)

angkatan_list = ["Semua Angkatan"] + sorted([str(x) for x in df_master["Angkatan"].dropna().unique().tolist()])
selected_angkatan = st.sidebar.selectbox("Angkatan", angkatan_list, index=0)

st.sidebar.markdown(
    clean_html(
        """
        <div style="font-size: 11px; color: #a8dadc; margin-top: 12px; line-height: 1.4;">
            Catatan: Filter di sidebar hanya berlaku untuk visualisasi deskriptif di halaman Overview dan Kendala.
        </div>
        """
    ),
    unsafe_allow_html=True,
)

# Terapkan filter ke dataframe
df_filtered = filter_data(df_master, fakultas=selected_fakultas, angkatan=selected_angkatan)

# Header Halaman
filter_desc = []
if selected_fakultas != "Semua Fakultas":
    filter_desc.append(selected_fakultas)
if selected_angkatan != "Semua Angkatan":
    filter_desc.append(f"Angkatan {selected_angkatan}")
subtitle_text = f"Populasi Kampus {CAMPUS_NAME}" + (f" (Filter: {', '.join(filter_desc)})" if filter_desc else " (Seluruh Mahasiswa)")

render_page_header(
    title="Overview: Lanskap Demografi & Akademik Kampus",
    subtitle=subtitle_text,
)

# Baris KPI Utama (Tier A resmi / filter dinamis)
n_mhs = len(df_filtered)
n_gen1 = (df_filtered["Status_Generasi_Pertama"] == "Ya").sum()
pct_gen1 = (n_gen1 / n_mhs * 100) if n_mhs > 0 else 0.0

ipk_avg = df_filtered["IPK_Mahasiswa"].mean() if n_mhs > 0 else 0.0

# Total kompetisi: jika tidak difilter gunakan sensus 6.414, jika difilter hitung transaksi mahasiswa terkait
if selected_fakultas == "Semua Fakultas" and selected_angkatan == "Semua Angkatan":
    total_kompetisi = len(df_prestasi)
else:
    mhs_ids = set(df_filtered["ID_Mahasiswa"])
    total_kompetisi = df_prestasi["ID_Mahasiswa"].isin(mhs_ids).sum()

gen1_mhs_filtered = df_filtered[df_filtered["Status_Generasi_Pertama"] == "Ya"]
if len(gen1_mhs_filtered) > 0:
    pct_gen1_mentored = (gen1_mhs_filtered["Ikut_Program_Pendampingan"] == "Ya").mean() * 100
else:
    pct_gen1_mentored = 0.0

kpi_cols = st.columns(5)
with kpi_cols[0]:
    render_kpi_card(
        label="Jumlah Mahasiswa",
        value=f"{n_mhs:,}",
        subtext=f"Total populasi {'terfilter' if filter_desc else 'kampus'}",
    )

with kpi_cols[1]:
    render_kpi_card(
        label="Proporsi Gen 1",
        value=f"{pct_gen1:.2f}%",
        subtext=f"{n_gen1:,} mahasiswa generasi pertama",
        highlight_diff="Pilar demografi",
    )

with kpi_cols[2]:
    render_kpi_card(
        label="Rata-rata IPK",
        value=f"{ipk_avg:.2f}",
        subtext="Skala standar 0,00 s.d. 4,00",
    )

with kpi_cols[3]:
    render_kpi_card(
        label="Kegiatan Kompetisi",
        value=f"{total_kompetisi:,}",
        subtext="Total transaksi partisipasi",
    )

with kpi_cols[4]:
    render_kpi_card(
        label="Gen 1 Ikut Bimbingan",
        value=f"{pct_gen1_mentored:.2f}%",
        subtext=f"{(gen1_mhs_filtered['Ikut_Program_Pendampingan'] == 'Ya').sum():,} mahasiswa didampingi",
    )

# Narasi tim
render_narrative_block(CONTENT["overview"]["ringkasan_populasi"])

# Bagian Visualisasi: Baris 1 (Komposisi & Distribusi IPK)
render_section_title("Distribusi Demografi dan Capaian Akademik")
chart_row1_col1, chart_row1_col2 = st.columns([1.1, 1.9])

with chart_row1_col1:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Komposisi Mahasiswa Generasi Pertama</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">Perbandingan Gen 1 vs Non-Gen 1</div>
        </div>
        """
    )
    st.plotly_chart(chart_komposisi_gen1(n_gen1, n_mhs - n_gen1), use_container_width=True)

with chart_row1_col2:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Distribusi IPK Akhir Mahasiswa</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">Pergeseran kurva nilai Gen 1 (merah) vs Non-Gen 1 (biru)</div>
        </div>
        """
    )
    st.plotly_chart(chart_distribusi_ipk(df_filtered), use_container_width=True)

# Bagian Visualisasi: Baris 2 (Angkatan & Fakultas)
chart_row2_col1, chart_row2_col2 = st.columns([1.3, 1.7])

with chart_row2_col1:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Sebaran Mahasiswa per Angkatan</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">Komposisi kohor 2019 hingga 2025</div>
        </div>
        """
    )
    st.plotly_chart(chart_sebaran_angkatan(df_filtered), use_container_width=True)

with chart_row2_col2:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Sebaran Mahasiswa per Fakultas</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">Jumlah mahasiswa di 15 fakultas universitas</div>
        </div>
        """
    )
    st.plotly_chart(chart_sebaran_fakultas(df_filtered), use_container_width=True)

# Bagian Visualisasi: Prestasi Per Tingkat
st_html(
    """
    <div style="margin-bottom: 4px;">
        <strong style="font-size: 14px; color: #1d3557;">Partisipasi Kegiatan Kompetisi per Tingkat</strong>
        <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">Total 6.414 kegiatan kompetisi (termasuk status Peserta)</div>
    </div>
    """
)
st.plotly_chart(chart_prestasi_per_tingkat(df_prestasi), use_container_width=True)

# Bagian Pertanyaan Kunci
render_section_title("Pertanyaan yang Masih Kami Cari Jawabannya")
st_html(
    """
    <p style="font-size: 14px; color: #475569; margin-bottom: 16px;">
        Data umum menunjukkan bahwa mahasiswa generasi pertama hadir dalam jumlah signifikan. Namun angka agregat awal ini membuka empat pertanyaan mendalam yang harus dibuktikan secara metodologis:
    </p>
    """
)

q_cols = st.columns(2)
questions = CONTENT["overview"]["pertanyaan_kunci"]["items"]

for idx, q in enumerate(questions):
    col = q_cols[idx % 2]
    with col:
        poin_text = " • ".join(q.get("poin_data", []))
        poin_html = f'<div style="font-size: 12px; color: #457b9d; margin-bottom: 14px; border-top: 1px solid rgba(168,218,220,0.3); padding-top: 8px;"><strong>Fakta Terkait:</strong> {poin_text}</div>' if poin_text else ""
        st_html(
            f"""
            <div class="saas-card" style="height: 100%; border-top: 3px solid {COLOR_PRIMARY};">
                <div style="font-size: 12px; font-weight: 700; color: {COLOR_PRIMARY}; margin-bottom: 6px;">PERTANYAAN {idx + 1}</div>
                <div style="font-size: 15px; font-weight: 700; color: {COLOR_TEXT}; margin-bottom: 8px; line-height: 1.4;">
                    {q['pertanyaan']}
                </div>
                <div style="font-size: 13.5px; color: #334155; line-height: 1.5; margin-bottom: 10px;">
                    {q['draf']}
                </div>
                {poin_html}
            </div>
            """
        )
        if st.button(q["tautan_teks"], key=f"q_btn_{idx}"):
            st.switch_page(f"pages/{q['tujuan_halaman']}")
