"""Halaman 3: Kendala - Realitas Ketimpangan & Beban Ganda Mahasiswa Gen 1.

Menyajikan analisis empiris kendala struktural:
- Kendala finansial (50,21% vs 22,17%)
- Beban ganda finansial & adaptasi (64,09% vs 43,17%, PR 1,48x)
- Defisit dukungan keluarga (2,84 vs 3,65)
- Kesenjangan IPK awal (2,99 vs 3,33, gap 0,35 poin)
Serta kotak callout 'Fokus Insight' yang mengarahkan pembaca ke Halaman 4.
Mendukung filter fakultas dan angkatan di sidebar untuk eksplorasi deskriptif.
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
    chart_komparasi_kendala_utama,
    chart_dukungan_keluarga_bar,
    chart_kesenjangan_ipk_gap,
)
from content import CONTENT

st.set_page_config(
    page_title=f"Kendala - {APP_TITLE}",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_custom_css()
render_sidebar_header()

# Pemuatan Data
df_master, _, _ = get_data()

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

df_filtered = filter_data(df_master, fakultas=selected_fakultas, angkatan=selected_angkatan)

filter_desc = []
if selected_fakultas != "Semua Fakultas":
    filter_desc.append(selected_fakultas)
if selected_angkatan != "Semua Angkatan":
    filter_desc.append(f"Angkatan {selected_angkatan}")
subtitle_text = f"Membedah Seberapa Berat Masalah dan Siapa yang Menanggungnya di {CAMPUS_NAME}" + (f" (Filter: {', '.join(filter_desc)})" if filter_desc else "")

render_page_header(
    title="Kendala: Beban Ganda Ketimpangan Generasi Pertama",
    subtitle=subtitle_text,
)

# Hitung Metrik Terfilter atau Gunakan Tier A Resmi
gen1_f = df_filtered[df_filtered["Status_Generasi_Pertama"] == "Ya"]
nongen1_f = df_filtered[df_filtered["Status_Generasi_Pertama"] == "Tidak"]

n_gen1 = len(gen1_f)
n_nongen1 = len(nongen1_f)

pct_fin_gen1 = (gen1_f["Kendala_Utama"] == "Finansial").mean() * 100 if n_gen1 > 0 else 50.21
pct_fin_nongen1 = (nongen1_f["Kendala_Utama"] == "Finansial").mean() * 100 if n_nongen1 > 0 else 22.17

pct_ganda_gen1 = gen1_f["Kendala_Utama"].isin(["Finansial", "Adaptasi"]).mean() * 100 if n_gen1 > 0 else 64.09
pct_ganda_nongen1 = nongen1_f["Kendala_Utama"].isin(["Finansial", "Adaptasi"]).mean() * 100 if n_nongen1 > 0 else 43.17

duk_gen1 = gen1_f["Tingkat_Dukungan_Keluarga"].mean() if n_gen1 > 0 else 2.84
duk_nongen1 = nongen1_f["Tingkat_Dukungan_Keluarga"].mean() if n_nongen1 > 0 else 3.65

ipk_gen1 = gen1_f["IPK_Mahasiswa"].mean() if n_gen1 > 0 else 2.99
ipk_nongen1 = nongen1_f["IPK_Mahasiswa"].mean() if n_nongen1 > 0 else 3.33
gap_ipk = ipk_nongen1 - ipk_gen1

# Baris KPI Ketimpangan (Tier A)
kpi_cols = st.columns(4)
with kpi_cols[0]:
    render_kpi_card(
        label="Kendala Biaya Gen 1",
        value=f"{pct_fin_gen1:.1f}%",
        subtext=f"Rekan lain hanya {pct_fin_nongen1:.1f}%",
        highlight_diff="2,3x lipat prevalensi",
    )

with kpi_cols[1]:
    render_kpi_card(
        label="Beban Ganda (Biaya & Adaptasi)",
        value=f"{pct_ganda_gen1:.1f}%",
        subtext=f"vs {pct_ganda_nongen1:.1f}% Non-Gen 1",
        highlight_diff="Rasio Prevalensi 1,48x lipat",
    )

with kpi_cols[2]:
    render_kpi_card(
        label="Dukungan Keluarga",
        value=f"{duk_gen1:.2f} / 5",
        subtext=f"Rekan lain {duk_nongen1:.2f} / 5,00",
        highlight_diff=f"Defisit {duk_gen1 - duk_nongen1:.2f} poin",
    )

with kpi_cols[3]:
    render_kpi_card(
        label="Kesenjangan IPK Kampus",
        value=f"{gap_ipk:.2f} Poin",
        subtext=f"Gen 1 ({ipk_gen1:.2f}) vs Non ({ipk_nongen1:.2f})",
        highlight_diff="Jurang kesenjangan nyata",
    )

# Narasi Tim untuk Beban Ganda
render_narrative_block(CONTENT["kendala"]["beban_ganda"])

# Baris Visualisasi 1: Komparasi Kendala Utama
render_section_title("Perbandingan Profil Kendala Utama")
st_html(
    """
    <div style="margin-bottom: 4px;">
        <strong style="font-size: 14px; color: #1d3557;">Persentase Mahasiswa Berdasarkan Kendala Utama</strong>
        <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">
            Gen 1 didominasi beban Finansial (50,2%), sedangkan Non-Gen 1 didominasi tantangan Akademik (38,9%)
        </div>
    </div>
    """
)
st.plotly_chart(chart_komparasi_kendala_utama(df_filtered), use_container_width=True)

# Narasi Tim untuk Beban Finansial
render_narrative_block(CONTENT["kendala"]["beban_finansial"])

# Baris Visualisasi 2: Dukungan Keluarga & Gap IPK Kampus
render_section_title("Defisit Dukungan Rumah & Kesenjangan Akademik Awal")
row2_c1, row2_c2 = st.columns([1.1, 0.9])

with row2_c1:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Skor Rata-rata Dukungan Edukatif Keluarga</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">
                Skala Likert survei (1 = sangat rendah, 5 = sangat tinggi)
            </div>
        </div>
        """
    )
    st.plotly_chart(chart_dukungan_keluarga_bar(), use_container_width=True)
    render_narrative_block(CONTENT["kendala"]["dukungan_keluarga"])

with row2_c2:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Kesenjangan IPK di Tingkat Universitas</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">
                Rata-rata IPK Non-Gen 1 (3,33) vs Gen 1 (2,99) menyisakan selisih 0,35 poin
            </div>
        </div>
        """
    )
    st.plotly_chart(chart_kesenjangan_ipk_gap(), use_container_width=True)
    render_narrative_block(CONTENT["kendala"]["kesenjangan_ipk"])

# Kotak Fokus Insight & Ajakan Membaca Halaman Insight
render_section_title("Jembatan ke Halaman Insight")
st_html(
    f"""
    <div style="background: #ffffff; border: 2px solid {COLOR_PRIMARY}; border-radius: 14px; padding: 22px 26px; box-shadow: 0 4px 16px rgba(29,53,87,0.08); margin: 20px 0;">
        <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: {COLOR_PRIMARY}; margin-bottom: 4px;">
            FOKUS INSIGHT
        </div>
        <div style="font-size: 18px; font-weight: 700; color: {COLOR_TEXT}; margin-bottom: 8px;">
            Apakah Program Pendampingan Kampus Mampu Mengimbangi Beban Berat Ini?
        </div>
        <p style="font-size: 14.5px; color: #334155; line-height: 1.6; margin-bottom: 0;">
            {CONTENT['kendala']['fokus_insight_callout']['teks']}
        </p>
    </div>
    """
)

if st.button("Telusuri Evaluasi & Nilai Tambah Terkontrol di Halaman Insight →", key="btn_go_insight"):
    st.switch_page("pages/4_Insight.py")
