"""Modul pemuatan, validasi, dan transformasi dataset resmi CDW 2026.

Memuat 5 file CSV dari data_set/, melakukan validasi baris dan relasi ID_Mahasiswa,
serta mereplikasi pembersihan dan rekayasa fitur sesuai notebook 01 dan 02.
Seluruh fungsi pemuatan di-cache menggunakan @st.cache_data.
"""

from pathlib import Path
from typing import Dict, Tuple, Optional
import pandas as pd
import numpy as np
import streamlit as st

from utils.config import DATA_FILES


def validate_row_counts(dfs: Dict[str, pd.DataFrame]) -> Tuple[bool, str]:
    """Validasi integritas jumlah baris kelima tabel mentah sesuai kamus data."""
    expected_counts = {
        "profil": 5000,
        "prestasi": 6414,
        "gen1": 5000,
        "sosek": 5000,
        "ipk": 25099,
    }
    
    for key, expected in expected_counts.items():
        if key not in dfs:
            return False, f"Tabel {key} tidak ditemukan dalam berkas dataset."
        actual = len(dfs[key])
        if actual != expected:
            return False, (
                f"Jumlah baris tabel {key} ({actual:,}) tidak cocok dengan spesifikasi ({expected:,})."
            )
    return True, "Validasi jumlah baris berhasil (semua tabel lengkap)."


@st.cache_data(show_spinner=False)
def load_and_process_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Memuat 5 tabel CSV mentah, membersihkan, dan menggabungkan menjadi tabel analitik.
    
    Returns:
        df_master: Tabel master tingkat mahasiswa (5.000 baris, fitur lengkap)
        df_ipk_long: Riwayat longitudinal IP semester (25.099 baris)
        df_prestasi_granular: Log kegiatan kompetisi (6.414 baris)
    """
    try:
        # 1. Pemuatan CSV dengan delimiter titik-koma (;)
        df_profil = pd.read_csv(DATA_FILES["profil"], sep=";")
        df_prestasi = pd.read_csv(DATA_FILES["prestasi"], sep=";")
        df_gen1 = pd.read_csv(DATA_FILES["gen1"], sep=";")
        df_sosek = pd.read_csv(DATA_FILES["sosek"], sep=";")
        df_ipk = pd.read_csv(DATA_FILES["ipk"], sep=";")
    except Exception as e:
        st.error(f"Gagal membaca file dataset: {e}. Pastikan seluruh file CSV berada di folder data_set/.")
        raise e

    # 2. Validasi jumlah baris
    is_valid, msg = validate_row_counts({
        "profil": df_profil,
        "prestasi": df_prestasi,
        "gen1": df_gen1,
        "sosek": df_sosek,
        "ipk": df_ipk,
    })
    if not is_valid:
        st.error(msg)
        raise ValueError(msg)

    # 3. Pembersihan spasi string pada setiap dataframe
    for df in [df_profil, df_prestasi, df_gen1, df_sosek, df_ipk]:
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].astype(str).str.strip()

    # 4. Pemrosesan tabel prestasi (agregasi per mahasiswa)
    capaian_rank = {"Juara 1": 5, "Juara 2": 4, "Juara 3": 3, "Finalis": 2, "Peserta": 1}
    tingkat_rank = {
        "Tingkat Internasional": 4,
        "Tingkat Nasional": 3,
        "Tingkat Lokal/Wilayah": 2,
        "Tingkat Kampus": 1,
    }

    df_prestasi_proc = df_prestasi.copy()
    df_prestasi_proc["_capaian_rank"] = df_prestasi_proc["Capaian_Prestasi"].map(capaian_rank)
    df_prestasi_proc["_tingkat_rank"] = df_prestasi_proc["Tingkat_Kegiatan"].map(tingkat_rank)

    prestasi_summary = df_prestasi_proc.groupby("ID_Mahasiswa").agg(
        Has_Prestasi=("ID_Mahasiswa", "count"),
        Jumlah_Prestasi=("ID_Mahasiswa", "count"),
        Prestasi_Tertinggi_Capaian=("_capaian_rank", "max"),
        Prestasi_Tertinggi_Tingkat=("_tingkat_rank", "max"),
        Punya_Prestasi_Internasional=("_tingkat_rank", lambda x: (x == 4).any()),
        Punya_Prestasi_Nasional=("_tingkat_rank", lambda x: (x >= 3).any()),
        Punya_Prestasi_Akademik=("Jenis_Prestasi", lambda x: (x == "Akademik").any()),
    ).reset_index()

    rank_to_capaian = {v: k for k, v in capaian_rank.items()}
    rank_to_tingkat = {v: k for k, v in tingkat_rank.items()}
    prestasi_summary["Prestasi_Tertinggi_Capaian_Label"] = prestasi_summary["Prestasi_Tertinggi_Capaian"].map(rank_to_capaian)
    prestasi_summary["Prestasi_Tertinggi_Tingkat_Label"] = prestasi_summary["Prestasi_Tertinggi_Tingkat"].map(rank_to_tingkat)
    prestasi_summary["Has_Prestasi"] = True

    # 5. Pemrosesan tabel riwayat IP semester
    df_ipk_sorted = df_ipk.sort_values(["ID_Mahasiswa", "Semester_Ke"])
    ipk_first = df_ipk_sorted.groupby("ID_Mahasiswa").first()[["IP_Semester", "IPK_Kumulatif"]].rename(
        columns={"IP_Semester": "IP_Semester_1", "IPK_Kumulatif": "IPK_Kum_Semester_1"}
    ).reset_index()

    ipk_last = df_ipk_sorted.groupby("ID_Mahasiswa").last()[["IP_Semester", "IPK_Kumulatif"]].rename(
        columns={"IP_Semester": "IP_Semester_Terakhir", "IPK_Kumulatif": "IPK_Kum_Akhir"}
    ).reset_index()

    ipk_stats = df_ipk_sorted.groupby("ID_Mahasiswa").agg(
        IP_Min=("IP_Semester", "min"),
        IP_Max=("IP_Semester", "max"),
        IP_Std=("IP_Semester", "std"),
        N_Semester=("Semester_Ke", "count"),
    ).reset_index()

    ipk_summary = ipk_first.merge(ipk_last, on="ID_Mahasiswa").merge(ipk_stats, on="ID_Mahasiswa")
    ipk_summary["Delta_IPK_Kumulatif"] = ipk_summary["IPK_Kum_Akhir"] - ipk_summary["IPK_Kum_Semester_1"]

    def kategorikan_tren(delta: float) -> str:
        if delta > 0.1:
            return "Naik"
        elif delta < -0.1:
            return "Turun"
        return "Stabil"

    ipk_summary["Tren_IPK"] = ipk_summary["Delta_IPK_Kumulatif"].apply(kategorikan_tren)

    # 6. Penggabungan tabel master
    df_gen1_join = df_gen1.copy()
    df_sosek_join = df_sosek.copy().rename(columns={"Sumber_Pembiayaan": "Sumber_Pembiayaan_Sosek"})

    df_master = (
        df_profil
        .merge(df_gen1_join, on="ID_Mahasiswa", how="inner")
        .merge(df_sosek_join, on="ID_Mahasiswa", how="inner")
        .merge(prestasi_summary, on="ID_Mahasiswa", how="left")
        .merge(ipk_summary, on="ID_Mahasiswa", how="left")
    )

    # Isi nilai default untuk mahasiswa tanpa rekaman prestasi
    df_master["Has_Prestasi"] = df_master["Has_Prestasi"].eq(True)
    df_master["Jumlah_Prestasi"] = df_master["Jumlah_Prestasi"].fillna(0).astype(int)
    df_master["Punya_Prestasi_Internasional"] = df_master["Punya_Prestasi_Internasional"].eq(True)
    df_master["Punya_Prestasi_Nasional"] = df_master["Punya_Prestasi_Nasional"].eq(True)
    df_master["Punya_Prestasi_Akademik"] = df_master["Punya_Prestasi_Akademik"].eq(True)

    # 7. Rekayasa fitur (Feature Engineering) sesuai notebook 02
    df_master["Kategori_Angkatan"] = pd.cut(
        df_master["Angkatan"],
        bins=[2018, 2021, 2025],
        labels=["Senior (2019–2021)", "Junior (2022–2025)"],
    )

    def kelompok_ipk(ipk: float) -> str:
        if pd.isna(ipk):
            return np.nan
        if ipk >= 3.50:
            return "Cumlaude (≥3.50)"
        elif ipk >= 3.00:
            return "Sangat Memuaskan (3.00–3.49)"
        elif ipk >= 2.50:
            return "Memuaskan (2.50–2.99)"
        return "Cukup (<2.50)"

    df_master["Kelompok_IPK"] = df_master["IPK_Mahasiswa"].apply(kelompok_ipk)

    df_master["Penerima_Beasiswa"] = df_master["Status_Penerima_Beasiswa"] == "Ya"
    df_master["Bekerja_Bool"] = df_master["Bekerja_Sambil_Kuliah"] == "Ya"
    df_master["Gen1_Bool"] = df_master["Status_Generasi_Pertama"] == "Ya"
    df_master["Ikut_Pendampingan_Bool"] = df_master["Ikut_Program_Pendampingan"] == "Ya"

    pendapatan_order = {
        "< Rp1.000.000": 1,
        "Rp1.000.000 - Rp3.000.000": 2,
        "Rp3.000.000 - Rp5.000.000": 3,
        "> Rp5.000.000": 4,
    }
    df_master["Pendapatan_Kategori_Urut"] = df_master["Pendapatan_Orang_Tua_per_Bulan"].map(pendapatan_order)

    def ukt_kategori(ukt: float) -> str:
        if pd.isna(ukt):
            return np.nan
        if ukt <= 3:
            return "Rendah (1–3)"
        elif ukt <= 5:
            return "Menengah (4–5)"
        return "Tinggi (6–8)"

    df_master["UKT_Kategori"] = df_master["Kategori_UKT"].apply(ukt_kategori)

    ip_rendah_pernah = df_ipk.groupby("ID_Mahasiswa")["IP_Semester"].apply(
        lambda x: (x < 2.0).any()
    ).reset_index()
    ip_rendah_pernah.columns = ["ID_Mahasiswa", "Pernah_IP_Rendah"]
    df_master = df_master.merge(ip_rendah_pernah, on="ID_Mahasiswa", how="left")

    ekonomi_order = pd.CategoricalDtype(categories=["Rendah", "Menengah", "Tinggi"], ordered=True)
    df_master["Kategori_Ekonomi_Ord"] = df_master["Kategori_Ekonomi"].astype(ekonomi_order)

    return df_master, df_ipk, df_prestasi


def get_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Titik akses publik pemanggilan data yang di-cache."""
    return load_and_process_data()


def filter_data(
    df: pd.DataFrame,
    fakultas: Optional[str] = "Semua Fakultas",
    angkatan: Optional[str] = "Semua Angkatan",
) -> pd.DataFrame:
    """Menerapkan filter fakultas dan angkatan pada tabel master."""
    filtered = df.copy()
    if fakultas and fakultas != "Semua Fakultas":
        filtered = filtered[filtered["Fakultas"] == fakultas]
    if angkatan and angkatan != "Semua Angkatan":
        # Handle string angkatan seperti "2021" atau integer
        try:
            angkatan_int = int(angkatan)
            filtered = filtered[filtered["Angkatan"] == angkatan_int]
        except ValueError:
            filtered = filtered[filtered["Angkatan"].astype(str) == str(angkatan)]
    return filtered
