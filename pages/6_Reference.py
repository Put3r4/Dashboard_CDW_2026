"""Halaman 6: Reference - Dokumentasi Teknis, Pipeline, Kode, & Audit V1-V12.

Menyajikan transparansi metodologis penuh:
- Stack teknologi & nomor versi pustaka
- Alur pipeline lima notebook (01 s.d. 05)
- Cuplikan kode terpilih (merge, Delta IPK, OLS HC3, IPW)
- Rekapitulasi 12 uji ketahanan (V1 s.d. V12)
- Definisi baku, kepatuhan etika data fiktif (RWFD), dan panduan replikasi lokal.
"""

import streamlit as st

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
    render_status_pill,
    render_narrative_block,
    render_callout,
    st_html,
)
from utils.results import ROBUSTNESS_CHECKS_SUMMARY
from content import CONTENT

st.set_page_config(
    page_title=f"Reference - {APP_TITLE}",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_custom_css()
render_sidebar_header()

# Header Halaman
render_page_header(
    title="Reference & Dokumentasi Metodologi",
    subtitle=f"Transparansi Teknis, Spesifikasi Pipeline, Cuplikan Model, dan Audit Ketahanan di {CAMPUS_NAME}",
)

# 1. Stack Teknologi
render_section_title("1. Lingkungan Komputasi & Pustaka Perangkat Lunak")
st_html(
    """
    <p style="font-size: 14px; color: #475569; margin-bottom: 12px;">
        Aplikasi dashboard dijalankan dengan pustaka produksi ringan untuk performa optimal, sementara model ekonometrika dihitung pada notebook analisis:
    </p>
    """
)

col_stack1, col_stack2 = st.columns(2)
with col_stack1:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 13px; font-weight: 700; color: #1d3557; margin-bottom: 8px;">Pustaka Dashboard (Runtime Web)</div>
            <table class="saas-table">
                <tr><th>Paket</th><th>Versi</th><th>Peran</th></tr>
                <tr><td><code>streamlit</code></td><td>1.51.0</td><td>Kerangka antarmuka interaktif</td></tr>
                <tr><td><code>pandas</code></td><td>2.x / 3.0.5</td><td>Manipulasi dataset tabular & caching</td></tr>
                <tr><td><code>plotly</code></td><td>6.3.0 / 5.18+</td><td>Grafik responsif tanpa modebar</td></tr>
                <tr><td><code>numpy</code></td><td>2.5.2 / 1.26+</td><td>Operasi array numerik</td></tr>
            </table>
        </div>
        """
    )

with col_stack2:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <div style="font-size: 13px; font-weight: 700; color: #1d3557; margin-bottom: 8px;">Pustaka Analisis & Audit Ekonometrika (Notebook)</div>
            <table class="saas-table">
                <tr><th>Paket</th><th>Versi</th><th>Peran</th></tr>
                <tr><td><code>statsmodels</code></td><td>0.14.5 / 0.15.0</td><td>Model OLS HC3 & regresi logistik</td></tr>
                <tr><td><code>scikit-learn</code></td><td>1.7.2</td><td>Estimasi Propensity Score bobot IPW</td></tr>
                <tr><td><code>scipy</code></td><td>1.16.3 / 1.18.0</td><td>Fisher Exact Test & t-test statistik</td></tr>
                <tr><td><code>python</code></td><td>3.10+ (3.12)</td><td>Bahasa pemrograman inti</td></tr>
            </table>
        </div>
        """
    )

# 2. Pipeline Lima Notebook
render_section_title("2. Alur Pipeline Analisis Data (Lima Notebook)")

pipeline_rows = ""
for item in CONTENT["reference"]["pipeline_notebook"]["items"]:
    pipeline_rows += f"""
    <tr>
        <td><code>{item['notebook']}</code></td>
        <td><strong>{item['tahap']}</strong></td>
        <td>{item['keluaran']}</td>
    </tr>
    """

st_html(
    f"""
    <table class="saas-table">
        <thead>
            <tr>
                <th style="width: 32%;">Nama Notebook</th>
                <th style="width: 28%;">Tahapan Analisis</th>
                <th style="width: 40%;">Keluaran Kunci</th>
            </tr>
        </thead>
        <tbody>
            {pipeline_rows}
        </tbody>
    </table>
    """
)

# 3. Cuplikan Kode Terpilih
render_section_title("3. Cuplikan Kode Model Terpilih (Reproducibility Snippets)")

tab_merge, tab_delta, tab_ols, tab_ipw = st.tabs([
    "Penggabungan Tabel",
    "Fitur Delta IPK",
    "Model OLS Galat HC3",
    "Penyeimbangan IPW",
])

with tab_merge:
    st.caption("Cuplikan logika penggabungan 5 tabel ke tabel master analitik (dari notebook 01):")
    st.code(
        """# Penggabungan multi-level 5 tabel administratif dan survei ke df_master
df_master = (
    df_profil
    .merge(df_gen1, on='ID_Mahasiswa', how='inner')
    .merge(df_sosek, on='ID_Mahasiswa', how='inner')
    .merge(prestasi_summary, on='ID_Mahasiswa', how='left')
    .merge(ipk_summary, on='ID_Mahasiswa', how='left')
)

# Penanganan nilai hilang untuk mahasiswa tanpa catatan lomba
df_master['Has_Prestasi'] = df_master['Has_Prestasi'].fillna(False).astype(bool)
df_master['Jumlah_Prestasi'] = df_master['Jumlah_Prestasi'].fillna(0).astype(int)""",
        language="python",
    )

with tab_delta:
    st.caption("Cuplikan perhitungan laju delta IPK kumulatif per individu (dari notebook 01):")
    st.code(
        """# Perhitungan laju pertumbuhan akademik dari semester 1 ke semester akhir
ipk_summary['Delta_IPK_Kumulatif'] = (
    ipk_summary['IPK_Kum_Akhir'] - ipk_summary['IPK_Kum_Semester_1']
)

def kategorikan_tren(delta):
    if delta > 0.1: return 'Naik'
    elif delta < -0.1: return 'Turun'
    return 'Stabil'

ipk_summary['Tren_IPK'] = ipk_summary['Delta_IPK_Kumulatif'].apply(kategorikan_tren)""",
        language="python",
    )

with tab_ols:
    st.caption("Spesifikasi model OLS nilai tambah terkontrol dengan galat baku robust MacKinnon-White HC3 (dari notebook 05, Uji V1):")
    st.code(
        """import statsmodels.formula.api as smf

# Model Nilai Tambah Terkontrol (Value-Added) pada seluruh Gen 1 (N = 1.924)
# Mengontrol nilai awal, angkatan, masa studi, fakultas, ekonomi, beasiswa, dan hunian
formula = (
    "IPK_Mahasiswa ~ C(Ikut_Program_Pendampingan) + IP_Semester_1 + "
    "C(Angkatan) + Masa_Studi_Semester + C(Fakultas) + "
    "C(Kategori_Ekonomi) + C(Status_Penerima_Beasiswa) + C(Tempat_Tinggal)"
)

model_ols = smf.ols(formula=formula, data=df_gen1).fit(cov_type="HC3")

# Koefisien pendampingan bersih: +0,0737 poin IPK (p = 2.02e-14, 95% CI [0.0548, 0.0926])
print(model_ols.summary())""",
        language="python",
    )

with tab_ipw:
    st.caption("Estimasi Propensity Score dan pembobotan Inverse Probability Weighting (dari notebook 05, Uji V3):")
    st.code(
        """from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm

# 1. Estimasi Propensity Score melalui Regresi Logistik
logit = LogisticRegression(max_iter=1000)
logit.fit(X_covariates, df_gen1['Ikut_Program_Pendampingan_Bool'])
ps = logit.predict_proba(X_covariates)[:, 1]

# 2. Perhitungan Bobot ATE (Average Treatment Effect)
T = df_gen1['Ikut_Program_Pendampingan_Bool'].astype(int)
w = (T / ps) + ((1 - T) / (1 - ps))

# 3. Estimasi Efek Tertimbang (Weighted Least Squares HC3)
# Hasil ATE Delta IPK: +0,0802 poin (p < 1e-9); seluruh post-SMD < 0,06""",
        language="python",
    )

# 4. Ringkasan 12 Uji Ketahanan (V1 s.d. V12)
render_section_title("4. Ringkasan Audit Ketahanan Skeptis (V1 s.d. V12)")

v_rows = ""
for item in ROBUSTNESS_CHECKS_SUMMARY:
    pill = render_status_pill(item["verdict"])
    v_rows += f"""
    <tr>
        <td style="font-weight: 700; color: #1d3557;"><code style="background: rgba(168,218,220,0.3); padding: 2px 6px; border-radius: 4px;">{item['kode']}</code></td>
        <td style="font-weight: 600; color: #1d3557;">{item['fokus']}</td>
        <td style="font-size: 13px; color: #334155;">{item['temuan']}</td>
        <td>{pill}</td>
    </tr>
    """

st_html(
    f"""
    <table class="saas-table">
        <thead>
            <tr>
                <th style="width: 10%;">Kode</th>
                <th style="width: 25%;">Fokus Pengujian</th>
                <th style="width: 50%;">Temuan Kunci Terkontrol</th>
                <th style="width: 15%;">Hasil Uji</th>
            </tr>
        </thead>
        <tbody>
            {v_rows}
        </tbody>
    </table>
    """
)

# 5. Definisi Baku & Catatan Etika
render_section_title("5. Definisi Baku, Etika Data, & Panduan Replikasi")

col_def1, col_def2 = st.columns(2)
with col_def1:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <strong style="font-size: 14px; color: #1d3557;">Definisi Operasional Baku</strong>
            <ul style="font-size: 13px; color: #334155; line-height: 1.5; padding-left: 18px; margin-top: 8px;">
                <li><strong>Partisipasi Kompetisi:</strong> Seluruh rekaman keikutsertaan lomba termasuk status 'Peserta' (Total universitas: 6.414 kegiatan; Gen 1: 1.305).</li>
                <li><strong>Kejuaraan Bersih:</strong> Hanya raihan medali Juara 1–3 dan Finalis (Total universitas: 4.599 kegiatan; Gen 1: 887).</li>
                <li><strong>Status Semester 8:</strong> Kohor mahasiswa yang menempuh semester 8 (N = 496), bukan jumlah lulusan resmi universitas.</li>
            </ul>
        </div>
        """
    )

with col_def2:
    st_html(
        """
        <div class="saas-card" style="height: 100%;">
            <strong style="font-size: 14px; color: #1d3557;">Panduan Replikasi Mandiri</strong>
            <p style="font-size: 13px; color: #334155; line-height: 1.5; margin-top: 8px;">
                Untuk menjalankan aplikasi secara lokal di lingkungan virtual:
            </p>
            <pre style="background: #f8fafc; border: 1px solid rgba(168,218,220,0.4); border-radius: 8px; padding: 10px; font-size: 12px; color: #1d3557;">pip install -r requirements.txt
streamlit run app.py</pre>
            <p style="font-size: 12px; color: #64748b; margin-bottom: 0;">
                Seluruh pengujian ekonometrika bersifat deterministik dengan seed tetap (seed = 42).
            </p>
        </div>
        """
    )

render_narrative_block(CONTENT["reference"]["etika_dan_reproduksi"])

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
if st.button("Kembali ke Halaman Selamat Datang →", key="btn_go_home"):
    st.switch_page("pages/1_Selamat_Datang.py")
