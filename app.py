"""Titik Masuk Utama Dashboard CDW 2026 - Universitas X.

Mengatur konfigurasi global, tema visual SaaS, dan mengarahkan navigasi awal
secara mulus ke Halaman 1 (Selamat Datang).
"""

from pathlib import Path
import streamlit as st

from utils.config import APP_TITLE, CAMPUS_NAME
from utils.components import apply_custom_css, render_sidebar_header

# Konfigurasi Halaman Global
st.set_page_config(
    page_title=f"{APP_TITLE} - {CAMPUS_NAME}",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Terapkan CSS dan Header Sidebar
apply_custom_css()
render_sidebar_header()

# Alihkan langsung ke halaman 1 (Selamat Datang)
try:
    st.switch_page("pages/1_Selamat_Datang.py")
except Exception:
    st.markdown(
        f"""
        <div style="text-align: center; padding: 60px 20px;">
            <h1 style="color: #1d3557; font-size: 28px;">{APP_TITLE}</h1>
            <p style="color: #457b9d; font-size: 16px;">{CAMPUS_NAME} - Campus Data Week 2026</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Masuk ke Halaman Selamat Datang →"):
        st.switch_page("pages/1_Selamat_Datang.py")
