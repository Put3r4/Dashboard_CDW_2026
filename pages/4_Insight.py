"""Halaman 4: Insight - Nilai Tambah Terkontrol & Evaluasi Metodologis Skeptis.

Halaman inti temuan data science:
1. Siapa yang ikut pendampingan (penyerapan kelompok rentan)
2. Hero Metric: Nilai tambah terkontrol +0,0737 poin IPK (OLS HC3 & IPW)
3. Lintasan panel longitudinal semester 1 s.d. 8 (N = 496) & catatan atrisi
4. Batas temuan: kesenjangan 0,33 poin belum tertutup & interaksi tidak signifikan
5. Tabel evaluasi "Klaim yang kami uji dan lepas" dengan pil status berwarna
6. Kotak penutup: "Apa yang bisa dan tidak bisa disimpulkan"
Bebas dari filter sidebar untuk menjamin integritas statistik inferensial.
"""

import streamlit as st
import pandas as pd

from utils.config import (
    APP_TITLE,
    CAMPUS_NAME,
    CONTROL_LABEL_HERO,
    COLOR_PRIMARY,
    COLOR_ACCENT,
    COLOR_TEXT,
    COLOR_MENTORED,
    COLOR_SECONDARY,
)
from utils.components import (
    apply_custom_css,
    render_sidebar_header,
    render_page_header,
    render_section_title,
    render_kpi_card,
    render_hero_metric_card,
    render_status_pill,
    render_narrative_block,
    render_callout,
    st_html,
    clean_html,
)
from utils.results import (
    N_TOTAL_MAHASISWA,
    GEN1_COUNT,
    MENTORED_GEN1_COUNT,
    MENTORED_GEN1_PCT,
    MENTORING_PENERIMA_BEASISWA_PCT,
    MENTORING_NON_BEASISWA_PCT,
    SMD_BEASISWA,
    MENTORING_DUKUNGAN_PESERTA,
    MENTORING_DUKUNGAN_NON,
    SMD_DUKUNGAN_KELUARGA,
    MENTORING_KENDALA_FINANSIAL_PCT,
    HERO_VALUE_ADDED_COEF,
    HERO_VALUE_ADDED_SE,
    HERO_VALUE_ADDED_CI,
    HERO_VALUE_ADDED_P,
    HERO_N,
    RAW_DELTA_DIFF,
    DECOMPOSITION_BASELINE_SHARE,
    DECOMPOSITION_VALUE_ADDED_SHARE,
    IPW_ATE_DELTA,
    IPW_ATE_DELTA_CI,
    IPW_ATE_DELTA_P,
    IPW_ATE_FINAL_GPA,
    IPW_ATE_FINAL_GPA_CI,
    IPW_ATE_FINAL_GPA_P,
    PANEL_N_TOTAL,
    PANEL_PESERTA_N,
    PANEL_NON_N,
    PANEL_DATA,
    PANEL_CUMULATIVE_SEM8_PESERTA,
    PANEL_CUMULATIVE_SEM8_NON,
    PERSISTENT_GAP_MENTORED_VS_NONGEN1,
    INTERACTION_BETA,
    INTERACTION_P,
    CLAIMS_EVALUATION_TABLE,
)
from utils.charts import (
    chart_penyerapan_pendampingan,
    chart_panel_longitudinal,
    chart_dekomposisi_laju,
    chart_komparasi_atrisi,
)
from content import CONTENT

st.set_page_config(
    page_title=f"Insight - {APP_TITLE}",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_custom_css()
render_sidebar_header()

# Header Halaman & Keterangan Bebas Filter
render_page_header(
    title="Insight: Pembuktian Nilai Tambah & Batas Temuan",
    subtitle=f"Audit Ekonometrika & Evaluasi Empiris Skeptis (V1 s.d. V12) di {CAMPUS_NAME}",
    unfilter_notice="Halaman ini menyajikan angka statistik inferensial yang telah tervalidasi uji ketahanan (V1 s.d. V12) dan tidak dipengaruhi oleh filter sidebar.",
)

# -----------------------------------------------------------------------------
# ALUR 1: SIAPA YANG IKUT PENDAMPINGAN? (PENYERAPAN KELOMPOK RENTAN)
# -----------------------------------------------------------------------------
render_section_title("1. Penjangkauan Program: Cenderung Menyerap Kelompok Rentan")

col_peny1, col_peny2, col_peny3, col_peny4 = st.columns(4)
with col_peny1:
    render_kpi_card(
        label="Penyerapan Gen 1",
        value=f"{MENTORED_GEN1_PCT:.2f}%",
        subtext=f"{MENTORED_GEN1_COUNT:,} dari {GEN1_COUNT:,} mahasiswa",
    )

with col_peny2:
    render_kpi_card(
        label="Penerima Beasiswa",
        value=f"{MENTORING_PENERIMA_BEASISWA_PCT:.1f}%",
        subtext=f"vs bukan beasiswa {MENTORING_NON_BEASISWA_PCT:.1f}%",
        highlight_diff=f"SMD = +{SMD_BEASISWA:.2f}",
    )

with col_peny3:
    render_kpi_card(
        label="Kendala Finansial",
        value=f"{MENTORING_KENDALA_FINANSIAL_PCT:.1f}%",
        subtext="555 dari 966 mahasiswa bertekanan biaya",
    )

with col_peny4:
    render_kpi_card(
        label="Dukungan Rumah Peserta",
        value=f"{MENTORING_DUKUNGAN_PESERTA:.2f}",
        subtext=f"vs non-peserta {MENTORING_DUKUNGAN_NON:.2f} / 5,00",
        highlight_diff=f"SMD = {SMD_DUKUNGAN_KELUARGA:.2f}",
    )

col_peny_chart, col_peny_notes = st.columns([1.2, 0.8])
with col_peny_chart:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Tingkat Partisipasi Pendampingan Berdasarkan Profil Kerentanan</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">
                Program secara alami menyerap mahasiswa penerima beasiswa dan berkendala biaya
            </div>
        </div>
        """
    )
    st.plotly_chart(chart_penyerapan_pendampingan(), use_container_width=True)

with col_peny_notes:
    render_callout(
        title="Bukan Seleksi Mahasiswa Pintar (Negative Selection)",
        text="Peserta pendampingan justru masuk dengan IP Semester 1 yang lebih rendah (2,62 vs 2,67). Program ini tidak mengalami bias seleksi ke mahasiswa yang sudah unggul sejak awal, melainkan menarik mahasiswa yang memang membutuhkan intervensi penopang.",
    )

render_narrative_block(CONTENT["insight"]["penjangkauan"])

# -----------------------------------------------------------------------------
# ALUR 2: HERO METRIC - NILAI TAMBAH TERKONTROL (UJI V1 & V3)
# -----------------------------------------------------------------------------
render_section_title("2. Hero Metric: Nilai Tambah Akademik Terkontrol (Value-Added)")

render_hero_metric_card(
    value=f"+{HERO_VALUE_ADDED_COEF:.3f} Poin IPK",
    title="Hero Metric Resmi (Model Nilai Tambah OLS HC3)",
    control_label=CONTROL_LABEL_HERO,
    ci_text=f"[{HERO_VALUE_ADDED_CI[0]:.4f}; {HERO_VALUE_ADDED_CI[1]:.4f}]",
    p_value_text=HERO_VALUE_ADDED_P,
    sub_badge="Konfirmasi Penyeimbangan IPW ATE: +0,0802 Poin Laju IPK (<em>p</em> &lt; 10<sup>&minus;9</sup>) & +0,0798 Poin IPK Akhir",
)

col_hero_c1, col_hero_c2 = st.columns([1.1, 0.9])
with col_hero_c1:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Dekomposisi Keunggulan Laju Kasar (+0,0934 Poin)</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">
                Mengapa klaim draf awal '+31,9% lebih cepat' harus diturunkan ke nilai tambah bersih +0,074 poin
            </div>
        </div>
        """
    )
    st.plotly_chart(chart_dekomposisi_laju(), use_container_width=True)

with col_hero_c2:
    st_html(
        f"""
        <div class="saas-card" style="height: 100%;">
            <strong style="font-size: 14px; color: #1d3557;">Arti Angka Kecil Ini bagi Mahasiswa</strong>
            <p style="font-size: 13.5px; color: #334155; line-height: 1.5; margin-top: 8px;">
                Angka <strong>+0,074 poin IPK</strong> sekilas terdengar kecil. Namun pada skala kumulatif 4 tahun, nilai ini mencerminkan kenaikan performa bersih yang konsisten di berbagai mata kuliah.
            </p>
            <p style="font-size: 13.5px; color: #334155; line-height: 1.5; margin-bottom: 0;">
                Audit dekomposisi membongkar bahwa <strong>{DECOMPOSITION_BASELINE_SHARE:.1f}%</strong> selisih laju kasar tercipta karena peserta mulai dari titik awal lebih rendah (-0,0532). Hanya <strong>{DECOMPOSITION_VALUE_ADDED_SHARE:.1f}%</strong> yang merupakan selisih nilai riil. Setelah seluruh faktor dikontrol, nilai tambah bersih tetap bertahan kokoh.
            </p>
        </div>
        """
    )

render_narrative_block(CONTENT["insight"]["hero_metric"])

# -----------------------------------------------------------------------------
# ALUR 3: LINTASAN PANEL LONGITUDINAL (N = 496) & CATATAN ATRISI (UJI V2 & V10)
# -----------------------------------------------------------------------------
render_section_title("3. Lintasan Panel Mahasiswa yang Mencapai Semester 8 (N = 496)")

st_html(
    """
    <div style="margin-bottom: 4px;">
        <strong style="font-size: 14px; color: #1d3557;">Trajektori Nilai Indeks Prestasi (IP) Semester Orang yang Sama</strong>
        <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">
            Melacak 496 mahasiswa Gen 1 secara konsisten dari Semester 1 hingga Semester 8 (252 peserta vs 244 non-peserta)
        </div>
    </div>
    """
)
st.plotly_chart(chart_panel_longitudinal(PANEL_DATA), use_container_width=True)

col_panel_stat1, col_panel_stat2 = st.columns([1.1, 0.9])
with col_panel_stat1:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <strong style="font-size: 14px; color: #1d3557;">Keunggulan Terkontrol IP Semester (Uji V2)</strong>
            <table class="saas-table" style="margin-top: 10px;">
                <tr><th>Tingkat Semester</th><th>Selisih Rerata</th><th>Terkontrol IP Sem 1 (HC3)</th><th>Signifikansi</th></tr>
                <tr><td>Semester 4</td><td>+0,099 poin</td><td><strong>+0,111 poin</strong></td><td><em>p</em> = 3,99 &times; 10<sup>&minus;4</sup></td></tr>
                <tr><td>Semester 6 (Puncak)</td><td>+0,219 poin</td><td><strong>+0,231 poin</strong></td><td><em>p</em> = 4,18 &times; 10<sup>&minus;14</sup></td></tr>
                <tr><td>Semester 8</td><td>+0,171 poin</td><td><strong>+0,182 poin</strong></td><td><em>p</em> = 9,69 &times; 10<sup>&minus;10</sup></td></tr>
            </table>
            <div style="font-size: 12px; color: #64748b; margin-top: 6px;">IPK Kumulatif Akhir Sem 8: Peserta 3,25 vs Non 3,13 (Selisih +0,12 poin)</div>
        </div>
        """
    )

with col_panel_stat2:
    st_html(
        """
        <div style="margin-bottom: 4px;">
            <strong style="font-size: 14px; color: #1d3557;">Catatan Kritis Seleksi Atrisi (Uji V10)</strong>
            <div style="font-size: 12px; color: #64748b; margin-bottom: 4px;">
                Komparasi status administratif mahasiswa pada akhir pemantauan
            </div>
        </div>
        """
    )
    st.plotly_chart(chart_komparasi_atrisi(), use_container_width=True)
    st_html(
        """
        <div style="font-size: 12px; color: #b91c1c; line-height: 1.4; border-top: 1px solid rgba(168,218,220,0.3); padding-top: 6px; margin-bottom: 12px;">
            Dilarang menggunakan istilah 'kelulusan' untuk panel Sem 8: peserta mengambil cuti studi 2x lebih tinggi (9,09% vs 4,77%) dan lulus resmi lebih rendah (15,84% vs 20,09%).
        </div>
        """
    )

render_narrative_block(CONTENT["insight"]["panel_longitudinal"])

# -----------------------------------------------------------------------------
# ALUR 4: BATAS TEMUAN - KESENJANGAN BELUM TERTUTUP (UJI V7)
# -----------------------------------------------------------------------------
render_section_title("4. Batas Temuan: Kesenjangan Akademik Belum Tertutup")

col_gap1, col_gap2 = st.columns([1.1, 0.9])
with col_gap1:
    render_callout(
        title="Jurang Kesenjangan 0,33 Poin Masih Membentang",
        text=f"Meskipun didampingi, mahasiswa generasi pertama membukukan IPK akhir 3,01—masih terpaut 0,33 poin di bawah rekan non-generasi pertama di angka 3,33. Pendampingan memperkecil jarak, namun belum menghapus disparitas kelas antargenerasi.",
        accent=True,
    )

with col_gap2:
    st_html(
        f"""
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 12px; font-weight: 700; color: #457b9d; margin-bottom: 4px;">UJI INTERAKSI REGRESI (N = 5.000)</div>
            <div style="font-size: 18px; font-weight: 700; color: #1d3557; margin-bottom: 6px;">
                Gen 1 &times; Pendampingan: <em>p</em> = {INTERACTION_P:.3f}
            </div>
            <p style="font-size: 13px; color: #475569; line-height: 1.4; margin-bottom: 0;">
                Koefisien interaksi tidak signifikan (&beta; = {INTERACTION_BETA:.4f}, <em>p</em> = 0,844). Ini membuktikan bahwa dorongan pendampingan (+0,077 poin) bersifat setara di seluruh populasi, tanpa adanya keajaiban penutupan kesenjangan khusus bagi Gen 1.
            </p>
        </div>
        """
    )

render_narrative_block(CONTENT["insight"]["batas_temuan"])

# -----------------------------------------------------------------------------
# ALUR 5: TABEL KLAIM YANG KAMI UJI DAN LEPAS (V1 s.d. V12)
# -----------------------------------------------------------------------------
render_section_title("5. Klaim yang Kami Uji dan Lepas (Transparansi Forensik)")

st_html(
    """
    <p style="font-size: 14px; color: #475569; margin-bottom: 12px;">
        Sebagai bentuk integritas sains data dan audit ketahanan skeptis, tim menguji klaim draf awal terhadap bukti data mentah. Klaim yang tidak lolos uji diturunkan atau digugurkan secara terbuka:
    </p>
    """
)

# Susun tabel HTML
rows_html = ""
for row in CLAIMS_EVALUATION_TABLE:
    pill_html = render_status_pill(row["status"])
    rows_html += f"""
    <tr>
        <td style="font-weight: 600; color: #1d3557;">{row['klaim']}</td>
        <td><strong>{row['evaluasi']}</strong></td>
        <td>{pill_html}</td>
        <td style="font-size: 13px; color: #475569;">{row['alasan']}</td>
        <td><code style="background: rgba(168,218,220,0.3); padding: 2px 6px; border-radius: 4px; color: #1d3557;">{row['kode']}</code></td>
    </tr>
    """

st_html(
    f"""
    <table class="saas-table">
        <thead>
            <tr>
                <th style="width: 25%;">Klaim Lama Proyek</th>
                <th style="width: 14%;">Evaluasi</th>
                <th style="width: 14%;">Status Uji</th>
                <th style="width: 37%;">Alasan Forensik Metodologis</th>
                <th style="width: 10%;">Kode Uji</th>
            </tr>
        </thead>
        <tbody>
            {rows_html}
        </tbody>
    </table>
    """
)

# -----------------------------------------------------------------------------
# ALUR 6: KOTAK PENUTUP - APA YANG BISA DAN TIDAK BISA DISIMPULKAN
# -----------------------------------------------------------------------------
render_section_title("6. Apa yang Bisa dan Tidak Bisa Disimpulkan")

bisa_list = "".join([f"<li style='margin-bottom: 6px;'>{item}</li>" for item in CONTENT["insight"]["kesimpulan_kotak"]["bisa_disimpulkan"]])
tidak_list = "".join([f"<li style='margin-bottom: 6px;'>{item}</li>" for item in CONTENT["insight"]["kesimpulan_kotak"]["tidak_bisa_disimpulkan"]])

col_concl1, col_concl2 = st.columns(2)
with col_concl1:
    st_html(
        f"""
        <div class="saas-card" style="height: 100%; border-top: 4px solid #059669;">
            <div style="font-size: 13px; font-weight: 700; color: #065f46; margin-bottom: 6px;">YANG BISA DISIMPULKAN (BERTAHAN)</div>
            <ul style="font-size: 13.5px; color: #334155; line-height: 1.5; padding-left: 20px; margin-top: 8px;">
                {bisa_list}
            </ul>
        </div>
        """
    )

with col_concl2:
    st_html(
        f"""
        <div class="saas-card" style="height: 100%; border-top: 4px solid #b91c1c;">
            <div style="font-size: 13px; font-weight: 700; color: #991b1b; margin-bottom: 6px;">YANG TIDAK BISA DISIMPULKAN (BATAS METODOLOGIS)</div>
            <ul style="font-size: 13.5px; color: #334155; line-height: 1.5; padding-left: 20px; margin-top: 8px;">
                {tidak_list}
            </ul>
        </div>
        """
    )

render_narrative_block(CONTENT["insight"]["kesimpulan_kotak"])

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
if st.button("Lanjutkan ke Halaman Kesimpulan & Rekomendasi Kebijakan →", key="btn_go_kesimpulan"):
    st.switch_page("pages/5_Kesimpulan.py")
