"""Halaman 5: Kesimpulan - Tiga Temuan Inti, Angka Sorotan, & Rekomendasi Kebijakan.

Menyajikan sintesis eksekutif bagi pengambil kebijakan kampus di Universitas X:
- Tiga temuan inti (demografi rentan, nilai tambah bersih, kesenjangan belum tuntas)
- Satu angka sorotan utama dengan label kontrol ketat (+0,074 poin IPK)
- Tiga rekomendasi kebijakan institusional berbasis bukti empiris.
"""

import streamlit as st

from utils.config import (
    APP_TITLE,
    CAMPUS_NAME,
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
    page_title=f"Kesimpulan - {APP_TITLE}",
    layout="wide",
    initial_sidebar_state="expanded",
)
apply_custom_css()
render_sidebar_header()

# Header Halaman
render_page_header(
    title="Kesimpulan & Rekomendasi Kebijakan",
    subtitle=f"Sintesis Temuan Empiris dan Arah Intervensi Berkelanjutan di {CAMPUS_NAME}",
)

# Tiga Poin Temuan Inti
render_section_title("Tiga Poin Temuan Inti")

cols = st.columns(3)
temuan_items = CONTENT["kesimpulan"]["tiga_temuan_inti"]["items"]

for idx, item in enumerate(temuan_items):
    with cols[idx]:
        st_html(
            f"""
            <div class="saas-card" style="height: 100%; border-top: 4px solid {COLOR_PRIMARY};">
                <div style="font-size: 12px; font-weight: 700; color: {COLOR_PRIMARY}; margin-bottom: 4px;">
                    POIN {item['nomor']}
                </div>
                <div style="font-size: 17px; font-weight: 700; color: {COLOR_TEXT}; margin-bottom: 10px; line-height: 1.3;">
                    {item['judul']}
                </div>
                <div style="font-size: 13.5px; color: #334155; line-height: 1.5; margin-bottom: 12px;">
                    {item['draf']}
                </div>
                <div style="font-size: 12px; color: #64748b; border-top: 1px solid rgba(168,218,220,0.3); padding-top: 8px;">
                    <strong>Fakta Kunci:</strong> {' • '.join(item['poin_data'])}
                </div>
            </div>
            """
        )

render_narrative_block(CONTENT["kesimpulan"]["tiga_temuan_inti"])

# Angka Sorotan Utama
render_section_title("Angka Sorotan Kebijakan")

st_html(
    f"""
    <div style="background: linear-gradient(135deg, #ffffff 0%, #f4f9fa 100%); border: 2px solid {COLOR_PRIMARY}; border-radius: 16px; padding: 28px 32px; box-shadow: 0 4px 18px rgba(29,53,87,0.08); text-align: center; margin-bottom: 24px;">
        <div style="font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: {COLOR_PRIMARY}; margin-bottom: 8px;">
            ANGKA SOROTAN UTAMA
        </div>
        <div style="font-size: 46px; font-weight: 800; color: {COLOR_TEXT}; line-height: 1.1; margin-bottom: 12px;">
            +0,074 Poin IPK
        </div>
        <div style="background: rgba(168, 218, 220, 0.25); border: 1px solid rgba(168, 218, 220, 0.8); border-radius: 8px; display: inline-block; padding: 8px 18px; font-size: 13px; font-weight: 500; color: {COLOR_TEXT}; margin-bottom: 12px;">
            {CONTROL_LABEL_HERO}
        </div>
        <p style="font-size: 14px; color: #475569; max-width: 720px; margin: 0 auto; line-height: 1.5;">
            Nilai tambah ini membuktikan bahwa intervensi pendampingan memberikan dorongan akademik nyata. Namun besaran angka ini sekaligus menegaskan bahwa bimbingan belajar tidak dapat bekerja sendiri tanpa sokongan bantalan ekonomi yang memadai.
        </p>
    </div>
    """
)

render_narrative_block(CONTENT["kesimpulan"]["angka_sorotan"])

# Rekomendasi Kebijakan
render_section_title("Usulan Rekomendasi Kebijakan Institusional")
st_html(
    """
    <p style="font-size: 14px; color: #475569; margin-bottom: 16px;">
        Berdasarkan temuan data, tim merumuskan tiga rekomendasi strategis bagi pengambil kebijakan di universitas:
    </p>
    """
)

rekomendasi_items = CONTENT["kesimpulan"]["rekomendasi"]["items"]
for idx, rek in enumerate(rekomendasi_items):
    st_html(
        f"""
        <div class="saas-card" style="margin-bottom: 16px;">
            <div style="display: flex; align-items: flex-start; gap: 14px;">
                <div style="background: {COLOR_PRIMARY}; color: #ffffff; width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; flex-shrink: 0;">
                    {idx + 1}
                </div>
                <div style="flex-grow: 1;">
                    <div style="font-size: 16px; font-weight: 700; color: {COLOR_TEXT}; margin-bottom: 6px;">
                        {rek['rekomendasi']}
                    </div>
                    <div style="font-size: 14px; color: #334155; line-height: 1.5; margin-bottom: 8px;">
                        {rek['draf']}
                    </div>
                    <div style="font-size: 12px; color: #64748b;">
                        <strong>Basis Data Empiris:</strong> {' • '.join(rek['poin_data'])}
                    </div>
                </div>
            </div>
        </div>
        """
    )

render_narrative_block(CONTENT["kesimpulan"]["rekomendasi"])

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
if st.button("Periksa Dokumentasi Teknis & Audit Ketahanan di Halaman Reference →", key="btn_go_reference"):
    st.switch_page("pages/6_Reference.py")
