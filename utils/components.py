"""Komponen UI dan CSS kustom bertema produk SaaS bersih untuk Dashboard CDW 2026.

Semua komponen mengikuti aturan ketat:
- Latar halaman: #f1faee, Kartu: #ffffff (radius 14px, bayangan lembut)
- Warna teks: #1d3557, Aksen: #e63946, Primer: #457b9d, Sekunder: #a8dadc
- Tidak ada emoji dan tidak ada ikon dekoratif
- Navigasi dan tombol menggunakan teks dan tanda panah (→)
- Pil status teks berwarna untuk verifikasi metodologis
"""

import re
import streamlit as st
from typing import Optional, List, Dict
from utils.config import (
    COLOR_BG,
    COLOR_CARD,
    COLOR_TEXT,
    COLOR_PRIMARY,
    COLOR_SECONDARY,
    COLOR_ACCENT,
    APP_TITLE,
    CAMPUS_NAME,
)


def apply_custom_css():
    """Menerapkan CSS global bertema SaaS modern, responsif, dan menyembunyikan elemen bawaan."""
    css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Reset & Tipografi */
    html, body, [class*="css"] {{
        font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        color: {COLOR_TEXT};
        background-color: {COLOR_BG};
    }}

    /* Latar Belakang Aplikasi */
    .stApp {{
        background-color: {COLOR_BG};
    }}

    /* Chrome bawaan Streamlit: sembunyikan toolbar dan menu, namun tampilkan tombol expand sidebar */
    header, header[data-testid="stHeader"], .stAppHeader {{
        background: transparent !important;
        color: {COLOR_TEXT} !important;
        z-index: 99990 !important;
        overflow: visible !important;
        pointer-events: auto !important;
    }}
    #MainMenu {{visibility: hidden !important;}}
    footer {{visibility: hidden !important;}}
    [data-testid="stDecoration"] {{display: none !important;}}
    [data-testid="stStatusWidget"] {{display: none !important;}}
    [data-testid="manage-app-button"] {{display: none !important;}}
    .stDeployButton {{display: none !important;}}
    [data-testid="stToolbarActions"] {{display: none !important;}}

    /* Tombol Buka/Tutup Sidebar Menu (stExpandSidebarButton dan stSidebarCollapsedControl) */
    [data-testid="stExpandSidebarButton"],
    [data-testid="stSidebarCollapsedControl"] {{
        display: inline-flex !important;
        visibility: visible !important;
        opacity: 1 !important;
        pointer-events: auto !important;
        align-items: center !important;
        justify-content: center !important;
        background-color: {COLOR_TEXT} !important;
        color: #ffffff !important;
        border: 2px solid {COLOR_SECONDARY} !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 14px rgba(29, 53, 87, 0.25) !important;
        padding: 6px 12px !important;
        margin-top: 8px !important;
        margin-left: 12px !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        z-index: 99999 !important;
    }}
    [data-testid="stExpandSidebarButton"]:hover,
    [data-testid="stSidebarCollapsedControl"]:hover {{
        background-color: {COLOR_PRIMARY} !important;
        border-color: #ffffff !important;
        transform: translateY(-1px) !important;
    }}
    [data-testid="stExpandSidebarButton"] svg,
    [data-testid="stSidebarCollapsedControl"] svg,
    [data-testid="stExpandSidebarButton"] span,
    [data-testid="stSidebarCollapsedControl"] span,
    [data-testid="stExpandSidebarButton"] *,
    [data-testid="stSidebarCollapsedControl"] * {{
        fill: #ffffff !important;
        stroke: #ffffff !important;
        color: #ffffff !important;
    }}

    /* Sidebar Kustom */
    [data-testid="stSidebar"] {{
        background-color: {COLOR_TEXT} !important;
        border-right: 1px solid rgba(168, 218, 220, 0.2);
    }}
    [data-testid="stSidebar"] * {{
        color: {COLOR_BG} !important;
    }}
    [data-testid="stSidebarNav"] a {{
        border-radius: 8px !important;
        margin: 2px 8px !important;
        padding: 8px 12px !important;
        transition: all 0.2s ease;
    }}
    [data-testid="stSidebarNav"] a:hover {{
        background-color: rgba(69, 123, 157, 0.4) !important;
    }}
    [data-testid="stSidebarNav"] a[aria-current="page"] {{
        background-color: {COLOR_PRIMARY} !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }}
    /* Sembunyikan titik masuk app dari daftar halaman sidebar */
    [data-testid="stSidebarNav"] ul li:first-child:has(a[href*="/app"]),
    [data-testid="stSidebarNav"] ul li:first-child:has(a[href$="/"]) {{
        display: none !important;
    }}

    /* Kartu Standar SaaS */
    .saas-card {{
        background: {COLOR_CARD};
        border-radius: 14px;
        box-shadow: 0 2px 12px rgba(29, 53, 87, 0.08);
        border: 1px solid rgba(168, 218, 220, 0.4);
        padding: 20px 24px;
        margin-bottom: 20px;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}
    .saas-card:hover {{
        box-shadow: 0 4px 18px rgba(29, 53, 87, 0.12);
    }}

    /* Kartu KPI */
    .kpi-container {{
        background: {COLOR_CARD};
        border-radius: 14px;
        box-shadow: 0 2px 12px rgba(29, 53, 87, 0.08);
        border: 1px solid rgba(168, 218, 220, 0.4);
        padding: 18px 20px;
        margin-bottom: 16px;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    .kpi-label {{
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        color: {COLOR_PRIMARY};
        margin-bottom: 6px;
    }}
    .kpi-value {{
        font-size: 30px;
        font-weight: 700;
        color: {COLOR_TEXT};
        line-height: 1.15;
        margin-bottom: 4px;
    }}
    .kpi-subtext {{
        font-size: 13px;
        color: #64748b;
        line-height: 1.3;
    }}
    .kpi-diff-highlight {{
        color: {COLOR_ACCENT};
        font-weight: 600;
    }}

    /* Hero Metric Card */
    .hero-card {{
        background: linear-gradient(135deg, #ffffff 0%, #f8fcfd 100%);
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(29, 53, 87, 0.10);
        border: 2px solid {COLOR_PRIMARY};
        padding: 28px 32px;
        margin-bottom: 24px;
        text-align: center;
    }}
    .hero-eyebrow {{
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: {COLOR_PRIMARY};
        margin-bottom: 8px;
    }}
    .hero-metric-val {{
        font-size: 44px;
        font-weight: 800;
        color: {COLOR_TEXT};
        line-height: 1.1;
        margin-bottom: 10px;
    }}
    .hero-control-label {{
        background: rgba(168, 218, 220, 0.25);
        border: 1px solid {COLOR_SECONDARY};
        border-radius: 8px;
        display: inline-block;
        padding: 8px 16px;
        font-size: 13px;
        font-weight: 500;
        color: {COLOR_TEXT};
        margin-top: 8px;
        margin-bottom: 12px;
        max-width: 90%;
    }}
    .hero-ci {{
        font-size: 14px;
        color: #475569;
        margin-top: 4px;
    }}

    /* Pil Status Metodologis */
    .status-pill {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        line-height: 1.2;
        letter-spacing: 0.3px;
    }}
    .pill-bertahan, .pill-kuat {{
        background-color: #d1fae5;
        color: #065f46;
        border: 1px solid #a7f3d0;
    }}
    .pill-melemah, .pill-terbatas {{
        background-color: #fef3c7;
        color: #92400e;
        border: 1px solid #fde68a;
    }}
    .pill-gugur {{
        background-color: #fee2e2;
        color: #991b1b;
        border: 1px solid #fecaca;
    }}
    .pill-batas {{
        background-color: #e0f2fe;
        color: #075985;
        border: 1px solid #bae6fd;
    }}

    /* Kotak Callout / Catatan */
    .callout-box {{
        background: #ffffff;
        border-left: 4px solid {COLOR_PRIMARY};
        border-radius: 0 12px 12px 0;
        padding: 16px 20px;
        box-shadow: 0 2px 8px rgba(29, 53, 87, 0.05);
        margin: 16px 0;
    }}
    .callout-box-accent {{
        background: #ffffff;
        border-left: 4px solid {COLOR_ACCENT};
        border-radius: 0 12px 12px 0;
        padding: 16px 20px;
        box-shadow: 0 2px 8px rgba(29, 53, 87, 0.05);
        margin: 16px 0;
    }}
    .callout-title {{
        font-weight: 700;
        font-size: 15px;
        color: {COLOR_TEXT};
        margin-bottom: 6px;
    }}
    .callout-text {{
        font-size: 14px;
        color: #334155;
        line-height: 1.5;
    }}

    /* Kotak Narasi Analisis Eksekutif */
    .narrative-block {{
        background: #ffffff;
        border-radius: 12px;
        border-left: 4px solid {COLOR_PRIMARY};
        box-shadow: 0 2px 10px rgba(29, 53, 87, 0.06);
        padding: 18px 22px;
        margin: 16px 0 22px 0;
    }}
    .narrative-tag {{
        display: inline-block;
        background: rgba(69, 123, 157, 0.12);
        color: {COLOR_PRIMARY};
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        padding: 3px 10px;
        border-radius: 6px;
    }}
    .narrative-text {{
        font-size: 14.5px;
        line-height: 1.65;
        color: #1e293b;
    }}
    .narrative-data-points {{
        font-size: 12.5px;
        color: #475569;
        margin-top: 10px;
        border-top: 1px solid rgba(168, 218, 220, 0.35);
        padding-top: 8px;
    }}

    /* Judul dan Hirarki Teks */
    .page-title {{
        font-size: 30px;
        font-weight: 800;
        color: {COLOR_TEXT};
        letter-spacing: -0.5px;
        margin-bottom: 4px;
    }}
    .page-subtitle {{
        font-size: 15px;
        color: #64748b;
        margin-bottom: 24px;
        line-height: 1.4;
    }}
    .section-title {{
        font-size: 20px;
        font-weight: 700;
        color: {COLOR_TEXT};
        margin-top: 24px;
        margin-bottom: 14px;
        letter-spacing: -0.2px;
    }}
    .unfilter-note {{
        font-size: 12px;
        color: #64748b;
        background: rgba(168, 218, 220, 0.2);
        display: inline-block;
        padding: 3px 10px;
        border-radius: 6px;
        margin-bottom: 16px;
    }}

    /* Tabel Kustom SaaS */
    .saas-table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid rgba(168, 218, 220, 0.4);
        background: #ffffff;
        margin: 16px 0;
    }}
    .saas-table th {{
        background: #f8fafc;
        color: {COLOR_TEXT};
        font-weight: 600;
        font-size: 13px;
        text-align: left;
        padding: 12px 16px;
        border-bottom: 1px solid rgba(168, 218, 220, 0.4);
    }}
    .saas-table td {{
        padding: 12px 16px;
        font-size: 13.5px;
        color: #334155;
        border-bottom: 1px solid rgba(168, 218, 220, 0.2);
        line-height: 1.4;
    }}
    .saas-table tr:last-child td {{
        border-bottom: none;
    }}
    .saas-table tr:hover td {{
        background-color: #f8fcfe;
    }}

    /* Penyesuaian Responsif Ponsel (390px) */
    @media (max-width: 640px) {{
        .hero-metric-val {{
            font-size: 34px;
        }}
        .hero-card {{
            padding: 20px 16px;
        }}
        .kpi-value {{
            font-size: 24px;
        }}
        .page-title {{
            font-size: 24px;
        }}
        .section-title {{
            font-size: 18px;
        }}
        .saas-card {{
            padding: 16px;
        }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def format_math_html(text: str) -> str:
    """Mengonversi notasi matematika/LaTeX ke format tipografi HTML yang elegan dan presisi."""
    if not text:
        return ""
    s = str(text)

    # 1. Bersihkan wrapper LaTeX \text{...} dan karakter khusus
    s = re.sub(r"\\text\{([^}]+)\}", r"\1", s)
    s = s.replace(r"\%", "%")
    s = s.replace("{,}", ",")
    s = re.sub(r"\\quad\\mid\\quad", " &nbsp;|&nbsp; ", s)
    s = s.replace(r"\mid", " | ")

    # 2. Simbol matematika Yunani dan operator
    s = s.replace(r"\times", "&times;")
    s = s.replace(r"\beta", "&beta;")
    s = s.replace(r"\alpha", "&alpha;")
    s = s.replace(r"\Delta", "&Delta;")
    s = s.replace(r"\pm", "&plusmn;")
    s = s.replace(r"\approx", "&asymp;")
    s = s.replace(r"\le", "&le;")
    s = s.replace(r"\ge", "&ge;")
    s = s.replace("--", "&ndash;")
    s = s.replace(r"\text{--}", "&ndash;")

    # 3. Notasi eksponen pangkat 10: 10^{-14}, 10^-14, 10^{14}, dll.
    s = re.sub(r"10\^\{-(\d+)\}", r"10<sup>&minus;\1</sup>", s)
    s = re.sub(r"10\^\{(\d+)\}", r"10<sup>\1</sup>", s)
    s = re.sub(r"10\^-(\d+)", r"10<sup>&minus;\1</sup>", s)
    s = re.sub(r"10\^(\d+)", r"10<sup>\1</sup>", s)

    # 4. Perkalian 10: ' x 10' atau '\times 10'
    s = re.sub(r"\s+[xX]\s+(10<sup>)", r" &times; \1", s)

    # 5. Subskrip: p_{holm} atau x_1
    s = re.sub(r"_\{([^}]+)\}", r"<sub>\1</sub>", s)

    # 6. Variabel matematika miring: p < , p = , r = (hanya jika diikuti angka/simbol matematika, bukan tag HTML!)
    s = re.sub(r"(?<![</a-zA-Z0-9_#&-])p\s*<\s*(?=[+-]?\d|10)", "<em>p</em> &lt; ", s)
    s = re.sub(r"(?<![</a-zA-Z0-9_#&-])p\s*>\s*(?=[+-]?\d|10)", "<em>p</em> &gt; ", s)
    s = re.sub(r"(?<![</a-zA-Z0-9_#&-])p\s*=\s*(?=[+-]?\d|10)", "<em>p</em> = ", s)
    s = re.sub(r"(?<![</a-zA-Z0-9_#&-])p\s*&le;\s*(?=[+-]?\d|10)", "<em>p</em> &le; ", s)
    s = re.sub(r"(?<![</a-zA-Z0-9_#&-])p\s*&ge;\s*(?=[+-]?\d|10)", "<em>p</em> &ge; ", s)
    s = re.sub(r"(?<![</a-zA-Z0-9_#&-])p(<sub>[^<]+</sub>)\s*=\s*(?=[+-]?\d|10)", r"<em>p</em>\1 = ", s)
    s = re.sub(r"(?<![</a-zA-Z0-9_#&-])r\s*=\s*(?=[+-]?\d)", "<em>r</em> = ", s)

    # 7. Minus sign dan stripping simbol dollar
    s = re.sub(r"\$([+-])", r"\1", s)
    s = s.replace("$", "")

    # 8. Bersihkan spasi ganda (tetap mempertahankan entitas HTML)
    s = re.sub(r"[ \t]+", " ", s).strip()
    return s


def clean_html(html_str: str) -> str:
    """Membersihkan string HTML dari indentasi, baris kosong, dan menstandarkan notasi matematika ke tipografi HTML."""
    lines = [line.strip() for line in html_str.splitlines() if line.strip()]
    cleaned = " ".join(lines)
    return format_math_html(cleaned)


def st_html(html_str: str):
    """Merender HTML secara aman tanpa risiko terformat sebagai blok kode di Streamlit."""
    st.markdown(clean_html(html_str), unsafe_allow_html=True)


def render_sidebar_header():
    """Merender tajuk sidebar statis teks saja tanpa emoji."""
    html = f"""
    <div style="padding: 16px 12px 8px 12px; border-bottom: 1px solid rgba(168,218,220,0.2); margin-bottom: 16px;">
        <div style="font-size: 17px; font-weight: 700; color: #f1faee; letter-spacing: -0.3px;">{APP_TITLE}</div>
        <div style="font-size: 12px; color: #a8dadc; margin-top: 2px;">{CAMPUS_NAME} - CDW 2026</div>
    </div>
    """
    st.sidebar.markdown(clean_html(html), unsafe_allow_html=True)


def render_page_header(
    title: str,
    subtitle: Optional[str] = None,
    unfilter_notice: Optional[str] = None,
    show_top_nav: bool = False,
):
    """Merender judul halaman, subjudul, dan catatan filter tanpa tombol navigasi atas (navigasi eksklusif via sidebar)."""
    st_html(f'<div class="page-title">{title}</div>')
    if subtitle:
        st_html(f'<div class="page-subtitle">{subtitle}</div>')
    if unfilter_notice:
        st_html(f'<div class="unfilter-note">{unfilter_notice}</div>')


def render_section_title(title: str):
    """Merender judul seksi berukuran 20px tebal teks bersih."""
    st_html(f'<div class="section-title">{title}</div>')


def render_kpi_card(label: str, value: str, subtext: Optional[str] = None, highlight_diff: Optional[str] = None):
    """Merender kartu KPI bergaya SaaS dengan angka besar dan keterangan perbandingan."""
    diff_html = f'<div class="kpi-diff-highlight">{highlight_diff}</div>' if highlight_diff else ""
    sub_html = f'<div class="kpi-subtext">{subtext}</div>' if subtext else ""
    html = f"""
    <div class="kpi-container">
        <div>
            <div class="kpi-label">{label}</div>
            <div class="kpi-value">{value}</div>
        </div>
        <div>
            {diff_html}
            {sub_html}
        </div>
    </div>
    """
    st_html(html)


def render_hero_metric_card(
    value: str,
    title: str,
    control_label: str,
    ci_text: str,
    p_value_text: str,
    sub_badge: Optional[str] = None,
):
    """Merender kartu Hero Metric utama dengan label kontrol ketat dan tipografi matematika presisi."""
    p_clean = format_math_html(p_value_text)
    ci_clean = f"95% CI {ci_text} &nbsp;|&nbsp; <em>p</em> = {p_clean}"
    badge_clean = format_math_html(sub_badge) if sub_badge else ""
    badge_html = f'<div style="font-size: 13.5px; color: {COLOR_PRIMARY}; font-weight: 600; margin-top: 8px;">{badge_clean}</div>' if badge_clean else ""
    html = f"""
    <div class="hero-card">
        <div class="hero-eyebrow">{title}</div>
        <div class="hero-metric-val">{value}</div>
        <div class="hero-control-label">{control_label}</div>
        <div class="hero-ci">{ci_clean}</div>
        {badge_html}
    </div>
    """
    st_html(html)


def render_status_pill(status: str) -> str:
    """Mengembalikan tag HTML untuk pil status teks berwarna."""
    status_lower = status.lower().strip()
    if "bertahan" in status_lower or "kuat" in status_lower:
        cls_name = "pill-bertahan"
    elif "melemah" in status_lower or "terbatas" in status_lower:
        cls_name = "pill-melemah"
    elif "gugur" in status_lower:
        cls_name = "pill-gugur"
    else:
        cls_name = "pill-batas"
    return f'<span class="status-pill {cls_name}">{status}</span>'


def render_narrative_block(draf_dict: Dict):
    """Merender blok narasi analisis resmi dengan tampilan kartu SaaS yang elegan."""
    title = draf_dict.get("title", "")
    teks = draf_dict.get("teks", "")
    poin_data = draf_dict.get("poin_data", [])

    poin_html = ""
    if poin_data:
        items = "".join([f"<li style='margin-bottom: 3px;'>{p}</li>" for p in poin_data])
        poin_html = f"""
        <div class="narrative-data-points">
            <strong style="color: {COLOR_TEXT};">Poin Data Terkait:</strong>
            <ul style="margin: 4px 0 2px 18px; padding: 0;">{items}</ul>
        </div>
        """

    html = f"""
    <div class="narrative-block">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <strong style="font-size: 15px; color: {COLOR_TEXT};">{title}</strong>
            <span class="narrative-tag">Narasi Analisis</span>
        </div>
        <div class="narrative-text">{teks}</div>
        {poin_html}
    </div>
    """
    st_html(html)


def render_callout(title: str, text: str, accent: bool = False):
    """Merender kotak callout teks informasi atau peringatan."""
    box_cls = "callout-box-accent" if accent else "callout-box"
    html = f"""
    <div class="{box_cls}">
        <div class="callout-title">{title}</div>
        <div class="callout-text">{text}</div>
    </div>
    """
    st_html(html)
