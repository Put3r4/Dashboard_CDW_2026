"""Modul visualisasi data Plotly bertema seragam SaaS untuk Dashboard CDW 2026.

Menerapkan palet resmi 5 warna konsisten:
- Latar: transparan / #ffffff
- Font: Inter, teks #1d3557
- Grid: #a8dadc (tipis)
- Gen 1 = #e63946, Non-Gen 1 = #457b9d
- Peserta pendampingan = #1d3557, Non-peserta = #a8dadc
Tanpa emoji, legenda di bawah, tanpa modebar yang mengganggu.
"""

from typing import List, Dict, Optional
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

from utils.config import (
    COLOR_BG,
    COLOR_CARD,
    COLOR_TEXT,
    COLOR_PRIMARY,
    COLOR_SECONDARY,
    COLOR_ACCENT,
    COLOR_GEN1,
    COLOR_NON_GEN1,
    COLOR_MENTORED,
    COLOR_NON_MENTORED,
)

# Konfigurasi interaksi default Plotly
PLOTLY_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
}


def apply_theme(fig: go.Figure, height: int = 380, show_legend: bool = True) -> go.Figure:
    """Menerapkan template visual SaaS konsisten ke objek figure Plotly."""
    fig.update_layout(
        font_family="Inter, system-ui, -apple-system, sans-serif",
        font_color=COLOR_TEXT,
        font_size=12,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        height=height,
        margin=dict(l=20, r=20, t=30, b=30),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.18,
            xanchor="center",
            x=0.5,
            font=dict(size=11, color=COLOR_TEXT),
            bgcolor="rgba(0,0,0,0)",
        ) if show_legend else dict(visible=False),
        hoverlabel=dict(
            bgcolor="#ffffff",
            font_size=12,
            font_family="Inter, system-ui, sans-serif",
            bordercolor=COLOR_PRIMARY,
        ),
    )
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(168, 218, 220, 0.4)",
        zeroline=False,
        tickfont=dict(size=11, color=COLOR_TEXT),
    )
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(168, 218, 220, 0.4)",
        zeroline=False,
        tickfont=dict(size=11, color=COLOR_TEXT),
    )
    return fig


# -----------------------------------------------------------------------------
# 1. Visualisasi Halaman Overview
# -----------------------------------------------------------------------------

def chart_komposisi_gen1(gen1_count: int = 1924, nongen1_count: int = 3076) -> go.Figure:
    """Donut chart proporsi Gen 1 vs Non-Gen 1 (Palet: Gen 1 = #e63946, Non = #457b9d)."""
    labels = ["Generasi Pertama (Gen 1)", "Bukan Generasi Pertama"]
    values = [gen1_count, nongen1_count]
    colors = [COLOR_GEN1, COLOR_NON_GEN1]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.62,
                marker=dict(colors=colors, line=dict(color="#ffffff", width=2)),
                textinfo="percent",
                textposition="inside",
                insidetextfont=dict(size=13, color="#ffffff", family="Inter"),
                hoverinfo="label+value+percent",
                direction="clockwise",
                sort=False,
            )
        ]
    )
    fig.update_layout(
        annotations=[
            dict(
                text=f"<b>38,5%</b><br><span style='font-size:11px; color:#64748b;'>Gen 1</span>",
                x=0.5,
                y=0.5,
                font=dict(size=20, color=COLOR_TEXT, family="Inter"),
                showarrow=False,
            )
        ]
    )
    return apply_theme(fig, height=300, show_legend=True)


def chart_sebaran_angkatan(df: pd.DataFrame) -> go.Figure:
    """Grafik batang sebaran mahasiswa per angkatan dengan pembagian Gen 1 vs Non-Gen 1."""
    grouped = df.groupby(["Angkatan", "Status_Generasi_Pertama"]).size().unstack(fill_value=0)
    
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=grouped.index.astype(str),
            y=grouped["Ya"],
            name="Generasi Pertama (Gen 1)",
            marker_color=COLOR_GEN1,
            text=grouped["Ya"],
            textposition="auto",
            textfont=dict(size=10, color="#ffffff"),
        )
    )
    fig.add_trace(
        go.Bar(
            x=grouped.index.astype(str),
            y=grouped["Tidak"],
            name="Non-Generasi Pertama",
            marker_color=COLOR_NON_GEN1,
            text=grouped["Tidak"],
            textposition="auto",
            textfont=dict(size=10, color="#ffffff"),
        )
    )
    fig.update_layout(
        barmode="stack",
        xaxis_title="Tahun Angkatan",
        yaxis_title="Jumlah Mahasiswa",
    )
    return apply_theme(fig, height=340)


def chart_sebaran_fakultas(df: pd.DataFrame) -> go.Figure:
    """Grafik batang horizontal jumlah mahasiswa per fakultas terurut."""
    fakultas_counts = df.groupby("Fakultas").size().sort_values(ascending=True)
    
    fig = go.Figure(
        go.Bar(
            x=fakultas_counts.values,
            y=fakultas_counts.index,
            orientation="h",
            marker_color=COLOR_PRIMARY,
            text=fakultas_counts.values,
            textposition="outside",
            textfont=dict(size=10, color=COLOR_TEXT),
            cliponaxis=False,
        )
    )
    fig.update_layout(
        xaxis_title="Jumlah Mahasiswa",
        yaxis_title="",
        margin=dict(l=140, r=40, t=10, b=30),
    )
    return apply_theme(fig, height=440, show_legend=False)


def chart_distribusi_ipk(df: pd.DataFrame) -> go.Figure:
    """Distribusi perbandingan IPK akhir mahasiswa Gen 1 vs Non-Gen 1."""
    gen1_ipk = df[df["Status_Generasi_Pertama"] == "Ya"]["IPK_Mahasiswa"]
    nongen1_ipk = df[df["Status_Generasi_Pertama"] == "Tidak"]["IPK_Mahasiswa"]

    fig = go.Figure()
    fig.add_trace(
        go.Histogram(
            x=gen1_ipk,
            name="Generasi Pertama (Rerata 2,99)",
            marker_color=COLOR_GEN1,
            opacity=0.75,
            nbinsx=25,
        )
    )
    fig.add_trace(
        go.Histogram(
            x=nongen1_ipk,
            name="Non-Generasi Pertama (Rerata 3,33)",
            marker_color=COLOR_NON_GEN1,
            opacity=0.65,
            nbinsx=25,
        )
    )
    fig.update_layout(
        barmode="overlay",
        xaxis_title="Indeks Prestasi Kumulatif (IPK)",
        yaxis_title="Frekuensi Mahasiswa",
    )
    return apply_theme(fig, height=330)


def chart_prestasi_per_tingkat(df_prestasi: pd.DataFrame) -> go.Figure:
    """Grafik batang horizontal raihan kegiatan kompetisi per tingkat."""
    counts = df_prestasi["Tingkat_Kegiatan"].value_counts().sort_values(ascending=True)
    
    fig = go.Figure(
        go.Bar(
            x=counts.values,
            y=counts.index,
            orientation="h",
            marker_color=COLOR_PRIMARY,
            text=[f"{v:,} ({v/len(df_prestasi)*100:.1f}%)" for v in counts.values],
            textposition="inside",
            insidetextfont=dict(color="#ffffff", size=11),
        )
    )
    fig.update_layout(
        xaxis_title="Jumlah Kegiatan Terdaftar",
        yaxis_title="",
        margin=dict(l=150, r=20, t=10, b=30),
    )
    return apply_theme(fig, height=260, show_legend=False)


# -----------------------------------------------------------------------------
# 2. Visualisasi Halaman Kendala
# -----------------------------------------------------------------------------

def chart_komparasi_kendala_utama(df: pd.DataFrame) -> go.Figure:
    """Perbandingan persentase kendala utama antara Gen 1 dan Non-Gen 1."""
    gen1 = df[df["Status_Generasi_Pertama"] == "Ya"]["Kendala_Utama"].value_counts(normalize=True) * 100
    nongen1 = df[df["Status_Generasi_Pertama"] == "Tidak"]["Kendala_Utama"].value_counts(normalize=True) * 100

    kategori = ["Finansial", "Akademik", "Adaptasi", "Sosial"]
    gen1_vals = [gen1.get(k, 0) for k in kategori]
    nongen1_vals = [nongen1.get(k, 0) for k in kategori]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=kategori,
            y=gen1_vals,
            name="Generasi Pertama (Gen 1)",
            marker_color=COLOR_GEN1,
            text=[f"{v:.1f}%" for v in gen1_vals],
            textposition="outside",
            textfont=dict(size=11, color=COLOR_GEN1, family="Inter"),
            cliponaxis=False,
        )
    )
    fig.add_trace(
        go.Bar(
            x=kategori,
            y=nongen1_vals,
            name="Non-Generasi Pertama",
            marker_color=COLOR_NON_GEN1,
            text=[f"{v:.1f}%" for v in nongen1_vals],
            textposition="outside",
            textfont=dict(size=11, color=COLOR_NON_GEN1, family="Inter"),
            cliponaxis=False,
        )
    )
    fig.update_layout(
        barmode="group",
        yaxis_title="Persentase Mahasiswa (%)",
        yaxis_range=[0, 60],
    )
    return apply_theme(fig, height=350)


def chart_dukungan_keluarga_bar() -> go.Figure:
    """Grafik batang komparasi rata-rata skor dukungan keluarga (Skala 1 - 5)."""
    kategori = ["Non-Generasi Pertama", "Generasi Pertama (Umum)", "Gen 1 Kendala Biaya"]
    skor = [3.65, 2.84, 2.67]
    warna = [COLOR_NON_GEN1, COLOR_GEN1, "#b91c1c"]

    fig = go.Figure(
        go.Bar(
            x=skor,
            y=kategori,
            orientation="h",
            marker_color=warna,
            text=[f"{s:.2f} / 5,00" for s in skor],
            textposition="outside",
            textfont=dict(size=11, color=COLOR_TEXT),
            cliponaxis=False,
        )
    )
    fig.update_layout(
        xaxis_title="Skor Dukungan Keluarga (1 - 5)",
        xaxis_range=[0, 5.2],
        yaxis_title="",
        margin=dict(l=160, r=50, t=10, b=30),
    )
    return apply_theme(fig, height=240, show_legend=False)


def chart_kesenjangan_ipk_gap() -> go.Figure:
    """Grafik batang perbandingan IPK rata-rata dan garis kesenjangan 0,35 poin."""
    kelompok = ["Non-Generasi Pertama", "Generasi Pertama"]
    ipk_val = [3.33, 2.99]

    fig = go.Figure(
        go.Bar(
            x=kelompok,
            y=ipk_val,
            marker_color=[COLOR_NON_GEN1, COLOR_GEN1],
            text=[f"{v:.2f}" for v in ipk_val],
            textposition="inside",
            insidetextfont=dict(color="#ffffff", size=14),
            width=0.45,
        )
    )
    # Garis anotasi kesenjangan
    fig.add_annotation(
        x=0.5,
        y=3.16,
        text="<b>Kesenjangan 0,35 poin</b>",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor=COLOR_ACCENT,
        font=dict(size=12, color=COLOR_ACCENT),
        bgcolor="#ffffff",
        bordercolor=COLOR_ACCENT,
        borderwidth=1,
    )
    fig.update_layout(
        yaxis_title="Rata-rata IPK",
        yaxis_range=[2.5, 3.6],
    )
    return apply_theme(fig, height=290, show_legend=False)


# -----------------------------------------------------------------------------
# 3. Visualisasi Halaman Insight
# -----------------------------------------------------------------------------

def chart_penyerapan_pendampingan() -> go.Figure:
    """Grafik batang horizontal penyerapan pendampingan pada subkelompok rentan."""
    kelompok = ["Penerima Beasiswa", "Bukan Penerima Beasiswa", "Kendala Biaya", "Dukungan Rendah (<3)"]
    pct_ikut = [62.76, 45.12, 57.45, 55.80]

    fig = go.Figure(
        go.Bar(
            x=pct_ikut,
            y=kelompok,
            orientation="h",
            marker_color=[COLOR_MENTORED, COLOR_SECONDARY, COLOR_MENTORED, COLOR_MENTORED],
            text=[f"{p:.1f}% Ikut" for p in pct_ikut],
            textposition="outside",
            textfont=dict(size=11, color=COLOR_TEXT),
            cliponaxis=False,
        )
    )
    fig.update_layout(
        xaxis_title="Persentase Mengikuti Pendampingan (%)",
        xaxis_range=[0, 75],
        yaxis_title="",
        margin=dict(l=170, r=60, t=10, b=30),
    )
    return apply_theme(fig, height=260, show_legend=False)


def chart_panel_longitudinal(panel_data: List[Dict]) -> go.Figure:
    """Grafik garis longitudinal panel seimbang N = 496 mahasiswa yang mencapai semester 8."""
    semesters = [f"Sem {d['semester']}" for d in panel_data]
    peserta_vals = [d["peserta"] for d in panel_data]
    non_vals = [d["non"] for d in panel_data]

    fig = go.Figure()

    # Garis Peserta Pendampingan (solid navy #1d3557)
    fig.add_trace(
        go.Scatter(
            x=semesters,
            y=peserta_vals,
            mode="lines+markers",
            name="Peserta Pendampingan (n = 252)",
            line=dict(color=COLOR_MENTORED, width=3),
            marker=dict(size=8, color=COLOR_MENTORED),
        )
    )

    # Garis Non-Peserta (putus-putus #a8dadc)
    fig.add_trace(
        go.Scatter(
            x=semesters,
            y=non_vals,
            mode="lines+markers",
            name="Bukan Peserta (n = 244)",
            line=dict(color=COLOR_PRIMARY, width=2.5, dash="dash"),
            marker=dict(size=7, color=COLOR_PRIMARY),
        )
    )

    # Callout anotasi titik balik dan keunggulan terkontrol
    fig.add_annotation(
        x="Sem 3",
        y=3.27,
        text="Titik Temu (+0,08)",
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-28,
        font=dict(size=10, color=COLOR_TEXT),
        bgcolor="#ffffff",
        bordercolor=COLOR_SECONDARY,
    )
    fig.add_annotation(
        x="Sem 6",
        y=3.45,
        text="Puncak (+0,231*)",
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-30,
        font=dict(size=10, color=COLOR_MENTORED),
        bgcolor="#ffffff",
        bordercolor=COLOR_MENTORED,
    )
    fig.add_annotation(
        x="Sem 8",
        y=3.44,
        text="Sem 8 (+0,182*)",
        showarrow=True,
        arrowhead=1,
        ax=0,
        ay=-26,
        font=dict(size=10, color=COLOR_MENTORED),
        bgcolor="#ffffff",
        bordercolor=COLOR_MENTORED,
    )

    fig.update_layout(
        xaxis_title="Semester Berjalan",
        yaxis_title="Indeks Prestasi (IP) Semester",
        yaxis_range=[2.60, 3.55],
    )
    return apply_theme(fig, height=360)


def chart_dekomposisi_laju() -> go.Figure:
    """Waterfall / Stacked bar dekomposisi keunggulan laju kasar (+0,0934 poin)."""
    fig = go.Figure(
        go.Bar(
            x=["Titik Start Rendah (56,9%)", "Nilai Tambah Akhir (43,1%)"],
            y=[0.0532, 0.0402],
            marker_color=[COLOR_SECONDARY, COLOR_PRIMARY],
            text=["0,0532 poin", "0,0402 poin"],
            textposition="auto",
            textfont=dict(size=12, color=COLOR_TEXT),
            width=0.45,
        )
    )
    fig.update_layout(
        yaxis_title="Kontribusi Selisih Poin IPK",
        yaxis_range=[0, 0.07],
    )
    return apply_theme(fig, height=280, show_legend=False)


def chart_komparasi_atrisi() -> go.Figure:
    """Grafik perbandingan status atrisi mahasiswa (V10)."""
    status = ["Cuti Kuliah", "Lulus Resmi", "DO / Non-Aktif"]
    peserta = [9.09, 15.84, 8.50]
    non = [4.77, 20.09, 7.55]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=status,
            y=peserta,
            name="Peserta Pendampingan",
            marker_color=COLOR_MENTORED,
            text=[f"{v:.1f}%" for v in peserta],
            textposition="outside",
            cliponaxis=False,
        )
    )
    fig.add_trace(
        go.Bar(
            x=status,
            y=non,
            name="Bukan Peserta",
            marker_color=COLOR_NON_MENTORED,
            text=[f"{v:.1f}%" for v in non],
            textposition="outside",
            cliponaxis=False,
        )
    )
    fig.update_layout(
        barmode="group",
        yaxis_title="Persentase (%)",
        yaxis_range=[0, 25],
    )
    return apply_theme(fig, height=300)
