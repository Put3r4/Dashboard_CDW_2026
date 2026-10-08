"""Skrip verifikasi dan pencocokan angka deskriptif dashboard vs Hasil_Analisis.md.

Membandingkan nilai hasil hitung langsung dari data mentah/olahan dengan angka Tier A.
Mencetak daftar status kecocokan untuk memastikan integritas single source of truth.
Bebas dari emoji sesuai pedoman tampilan proyek.
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Tambahkan direktori root ke sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from utils.data_loader import load_and_process_data


def run_checks():
    print("=" * 78)
    print("AUDIT KETERTELUSURAN ANGKA DASHBOARD CDW 2026")
    print("Membandingkan Hasil Hitung Langsung vs. Dokumen Resmi (Hasil_Analisis.md)")
    print("=" * 78)

    df_master, df_ipk, df_prestasi = load_and_process_data()

    checks = []

    def add_check(kode, nama_metrik, nilai_hitung, nilai_target, format_str="{:.2f}", tol=0.01):
        if isinstance(nilai_target, (int, np.integer)):
            diff = abs(nilai_hitung - nilai_target)
            cocok = (diff == 0)
            str_hitung = f"{int(nilai_hitung):,}"
            str_target = f"{int(nilai_target):,}"
        elif isinstance(nilai_target, float):
            diff = abs(nilai_hitung - nilai_target)
            cocok = (diff <= tol)
            str_hitung = format_str.format(nilai_hitung)
            str_target = format_str.format(nilai_target)
        else:
            cocok = (str(nilai_hitung) == str(nilai_target))
            str_hitung = str(nilai_hitung)
            str_target = str(nilai_target)

        status_str = "[COCOK]" if cocok else "[TIDAK COCOK]"
        checks.append({
            "kode": kode,
            "metrik": nama_metrik,
            "hitung": str_hitung,
            "target": str_target,
            "status": status_str,
            "is_match": cocok,
        })

    # 1. Skala Demografi (A1 - A3)
    n_total = len(df_master)
    add_check("A1", "Total Mahasiswa Kampus", n_total, 5000)

    gen1_mhs = df_master[df_master["Status_Generasi_Pertama"] == "Ya"]
    nongen1_mhs = df_master[df_master["Status_Generasi_Pertama"] == "Tidak"]

    n_gen1 = len(gen1_mhs)
    pct_gen1 = (n_gen1 / n_total) * 100
    add_check("A2", "Jumlah Mahasiswa Gen 1", n_gen1, 1924)
    add_check("A2", "Proporsi Mahasiswa Gen 1 (%)", pct_gen1, 38.48, "{:.2f}%")

    n_nongen1 = len(nongen1_mhs)
    pct_nongen1 = (n_nongen1 / n_total) * 100
    add_check("A3", "Jumlah Mahasiswa Non-Gen 1", n_nongen1, 3076)
    add_check("A3", "Proporsi Mahasiswa Non-Gen 1 (%)", pct_nongen1, 61.52, "{:.2f}%")

    # 2. Kendala dan Beban (B1 - B9)
    kendala_fin_gen1 = (gen1_mhs["Kendala_Utama"] == "Finansial").sum()
    pct_fin_gen1 = (kendala_fin_gen1 / n_gen1) * 100
    add_check("B1", "Gen 1 Kendala Finansial (%)", pct_fin_gen1, 50.21, "{:.2f}%")

    kendala_fin_nongen1 = (nongen1_mhs["Kendala_Utama"] == "Finansial").sum()
    pct_fin_nongen1 = (kendala_fin_nongen1 / n_nongen1) * 100
    add_check("B6", "Non-Gen 1 Kendala Finansial (%)", pct_fin_nongen1, 22.17, "{:.2f}%")

    beban_ganda_gen1 = gen1_mhs["Kendala_Utama"].isin(["Finansial", "Adaptasi"]).sum()
    pct_ganda_gen1 = (beban_ganda_gen1 / n_gen1) * 100
    add_check("B5", "Beban Ganda Gen 1: Finansial & Adaptasi (%)", pct_ganda_gen1, 64.09, "{:.2f}%")
    add_check("B5", "Jumlah Mahasiswa Beban Ganda Gen 1", beban_ganda_gen1, 1233)

    beban_ganda_nongen1 = nongen1_mhs["Kendala_Utama"].isin(["Finansial", "Adaptasi"]).sum()
    pct_ganda_nongen1 = (beban_ganda_nongen1 / n_nongen1) * 100
    add_check("V8", "Beban Ganda Non-Gen 1 (%)", pct_ganda_nongen1, 43.17, "{:.2f}%")

    duk_gen1 = gen1_mhs["Tingkat_Dukungan_Keluarga"].mean()
    duk_nongen1 = nongen1_mhs["Tingkat_Dukungan_Keluarga"].mean()
    add_check("B7", "Skor Dukungan Keluarga Gen 1", duk_gen1, 2.84, "{:.2f}")
    add_check("B8", "Skor Dukungan Keluarga Non-Gen 1", duk_nongen1, 3.65, "{:.2f}")

    duk_gen1_fin = gen1_mhs[gen1_mhs["Kendala_Utama"] == "Finansial"]["Tingkat_Dukungan_Keluarga"].mean()
    add_check("B9", "Dukungan Gen 1 Kendala Finansial", duk_gen1_fin, 2.67, "{:.2f}")

    # 3. Kesenjangan IPK Kampus (E1)
    ipk_kampus = df_master["IPK_Mahasiswa"].mean()
    ipk_nongen1 = nongen1_mhs["IPK_Mahasiswa"].mean()
    ipk_gen1 = gen1_mhs["IPK_Mahasiswa"].mean()
    gap_ipk = ipk_nongen1 - ipk_gen1
    add_check("E1", "Rata-rata IPK Mahasiswa Non-Gen 1", ipk_nongen1, 3.33, "{:.2f}")
    add_check("E1", "Rata-rata IPK Mahasiswa Gen 1", ipk_gen1, 2.99, "{:.2f}")
    add_check("E1", "Kesenjangan IPK Kampus (Poin)", gap_ipk, 0.35, "{:.2f}")

    # 4. Penyerapan Pendampingan (C1 - C8)
    ment_ya = gen1_mhs[gen1_mhs["Ikut_Program_Pendampingan"] == "Ya"]
    ment_tdk = gen1_mhs[gen1_mhs["Ikut_Program_Pendampingan"] == "Tidak"]
    n_ment_ya = len(ment_ya)
    pct_ment_ya = (n_ment_ya / n_gen1) * 100
    add_check("C1", "Jumlah Gen 1 Peserta Pendampingan", n_ment_ya, 1023)
    add_check("C1", "Proporsi Gen 1 Ikut Pendampingan (%)", pct_ment_ya, 53.17, "{:.2f}%")

    ipk_akhir_ya = ment_ya["IPK_Mahasiswa"].mean()
    ipk_akhir_tdk = ment_tdk["IPK_Mahasiswa"].mean()
    add_check("C3", "IPK Akhir Gen 1 Peserta", ipk_akhir_ya, 3.01, "{:.2f}")
    add_check("C4", "IPK Akhir Gen 1 Non-Peserta", ipk_akhir_tdk, 2.97, "{:.2f}")

    delta_ya = ment_ya["Delta_IPK_Kumulatif"].mean()
    delta_tdk = ment_tdk["Delta_IPK_Kumulatif"].mean()
    delta_diff = delta_ya - delta_tdk
    add_check("C6", "Rata-rata Laju Delta IPK Peserta", delta_ya, 0.3864, "{:.4f}")
    add_check("C7", "Rata-rata Laju Delta IPK Non-Peserta", delta_tdk, 0.2930, "{:.4f}")
    add_check("C8", "Keunggulan Laju Kasar (Poin)", delta_diff, 0.0934, "{:.4f}")

    # 5. Prestasi dan Rekonsiliasi V11
    total_kegiatan = len(df_prestasi)
    add_check("V11", "Total Seluruh Kegiatan Kompetisi", total_kegiatan, 6414)

    kejuaraan_bersih_total = df_prestasi["Capaian_Prestasi"].isin(["Juara 1", "Juara 2", "Juara 3", "Finalis"]).sum()
    add_check("V11", "Total Raihan Kejuaraan Bersih Kampus", kejuaraan_bersih_total, 4599)

    df_p_mhs = df_prestasi.merge(df_master[["ID_Mahasiswa", "Status_Generasi_Pertama", "Ikut_Program_Pendampingan"]], on="ID_Mahasiswa")
    p_gen1 = df_p_mhs[df_p_mhs["Status_Generasi_Pertama"] == "Ya"]
    p_nongen1 = df_p_mhs[df_p_mhs["Status_Generasi_Pertama"] == "Tidak"]
    add_check("V11", "Transaksi Partisipasi Non-Gen 1", len(p_nongen1), 5109)
    add_check("V11", "Transaksi Partisipasi Gen 1", len(p_gen1), 1305)

    kejuaraan_bersih_gen1 = p_gen1["Capaian_Prestasi"].isin(["Juara 1", "Juara 2", "Juara 3", "Finalis"]).sum()
    add_check("V11", "Kejuaraan Bersih Gen 1", kejuaraan_bersih_gen1, 887)

    has_pres_ya = ment_ya["Has_Prestasi"].mean() * 100
    has_pres_tdk = ment_tdk["Has_Prestasi"].mean() * 100
    add_check("D1", "Proporsi Has_Prestasi Peserta (%)", has_pres_ya, 39.69, "{:.2f}%")
    add_check("D2", "Proporsi Has_Prestasi Non-Peserta (%)", has_pres_tdk, 44.73, "{:.2f}%")

    p_gen1_ya = p_gen1[p_gen1["Ikut_Program_Pendampingan"] == "Ya"]
    p_gen1_tdk = p_gen1[p_gen1["Ikut_Program_Pendampingan"] == "Tidak"]
    pct_inter_ya = (p_gen1_ya["Tingkat_Kegiatan"] == "Tingkat Internasional").mean() * 100
    pct_inter_tdk = (p_gen1_tdk["Tingkat_Kegiatan"] == "Tingkat Internasional").mean() * 100
    add_check("D4", "Kegiatan Internasional Gen 1 Peserta (%)", pct_inter_ya, 6.95, "{:.2f}%")
    add_check("D4", "Kegiatan Internasional Gen 1 Non-Peserta (%)", pct_inter_tdk, 5.06, "{:.2f}%")

    # 6. Panel Seimbang Semester 8 (V2, N = 496)
    mhs_sem8 = df_ipk[df_ipk["Semester_Ke"] == 8]["ID_Mahasiswa"].unique()
    gen1_sem8_ids = gen1_mhs[gen1_mhs["ID_Mahasiswa"].isin(mhs_sem8)]["ID_Mahasiswa"].tolist()
    add_check("V2", "Panel Seimbang Gen 1 Semester 8 (N)", len(gen1_sem8_ids), 496)

    # Cetak hasil verifikasi
    print(f"{'Kode':<6} {'Nama Indikator / Metrik':<42} {'Hitung':>12} {'Target':>12} {'Status':>14}")
    print("-" * 90)
    all_matched = True
    for c in checks:
        if not c["is_match"]:
            all_matched = False
        print(f"{c['kode']:<6} {c['metrik']:<42} {c['hitung']:>12} {c['target']:>12} {c['status']:>14}")

    print("=" * 90)
    total_checks = len(checks)
    matched_count = sum(1 for c in checks if c["is_match"])
    print(f"Hasil Audit: {matched_count} dari {total_checks} metrik cocok ({matched_count/total_checks*100:.1f}%)")
    if all_matched:
        print("STATUS FINAL: SEMUA ANGKA DESKRIPTIF COCOK 100% DENGAN TIER A.")
    else:
        print("PERINGATAN: TERDAPAT KETIDAKCOCOKAN PADA METRIK DI ATAS.")
    print("=" * 90)
    return all_matched


if __name__ == "__main__":
    success = run_checks()
    sys.exit(0 if success else 1)
