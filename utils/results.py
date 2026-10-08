"""Hasil analisis inferensial dan audit ketahanan data (V1 s.d. V12) yang telah tervalidasi.

Statistik inferensial disimpan sebagai konstanta teruji agar aplikasi Streamlit
berjalan ringan tanpa komputasi regresi berulang saat dimuat.
Rujukan: Validasi_Data.md dan Hasil_Analisis.md.
"""

# -------------------------------------------------------------------------
# 1. Metrik Skala Demografi (Tier A)
# -------------------------------------------------------------------------
N_TOTAL_MAHASISWA = 5000

GEN1_COUNT = 1924
GEN1_PCT = 38.48

NON_GEN1_COUNT = 3076
NON_GEN1_PCT = 61.52

# -------------------------------------------------------------------------
# 2. Ketimpangan Struktural & Beban Ganda (Tier A)
# -------------------------------------------------------------------------
DUAL_BURDEN_GEN1_PCT = 64.09
DUAL_BURDEN_GEN1_N = 1233

DUAL_BURDEN_NONGEN1_PCT = 43.17
DUAL_BURDEN_NONGEN1_N = 1328

PREVALENCE_RATIO_BURDEN = 1.4844
CI_PREVALENCE_BURDEN = (1.4084, 1.5645)
P_VALUE_BURDEN = r"< 10^{-15}"

KENDALA_FINANSIAL_GEN1_PCT = 50.21
KENDALA_FINANSIAL_GEN1_N = 966
KENDALA_FINANSIAL_NONGEN1_PCT = 22.17
KENDALA_FINANSIAL_NONGEN1_N = 682

KENDALA_AKADEMIK_GEN1_PCT = 26.98
KENDALA_AKADEMIK_GEN1_N = 519
KENDALA_AKADEMIK_NONGEN1_PCT = 38.85
KENDALA_AKADEMIK_NONGEN1_N = 1195

KENDALA_ADAPTASI_GEN1_PCT = 13.88
KENDALA_ADAPTASI_GEN1_N = 267
KENDALA_ADAPTASI_NONGEN1_PCT = 21.00
KENDALA_ADAPTASI_NONGEN1_N = 646

KENDALA_SOSIAL_GEN1_PCT = 8.94
KENDALA_SOSIAL_GEN1_N = 172
KENDALA_SOSIAL_NONGEN1_PCT = 17.98
KENDALA_SOSIAL_NONGEN1_N = 553

DUKUNGAN_KELUARGA_GEN1_MEAN = 2.8415
DUKUNGAN_KELUARGA_GEN1_STD = 1.0934
DUKUNGAN_KELUARGA_NONGEN1_MEAN = 3.6460
DUKUNGAN_KELUARGA_NONGEN1_STD = 1.0242
DUKUNGAN_KELUARGA_DIFF = -0.8045
CI_DUKUNGAN_KELUARGA = (-0.87, -0.75)
P_VALUE_DUKUNGAN = r"< 10^{-15}"
DUKUNGAN_KELUARGA_GEN1_FINANSIAL = 2.6708

# -------------------------------------------------------------------------
# 3. Kesenjangan IPK Kampus (Tier A)
# -------------------------------------------------------------------------
IPK_KAMPUS_MEAN = 3.2007
IPK_NON_GEN1_MEAN = 3.3348
IPK_GEN1_MEAN = 2.9869
IPK_GAP_KAMPUS = 0.3479  # 0,35 poin

# -------------------------------------------------------------------------
# 4. Penyerapan Program Pendampingan (Tier A)
# -------------------------------------------------------------------------
MENTORED_GEN1_COUNT = 1023
MENTORED_GEN1_PCT = 53.17

NON_MENTORED_GEN1_COUNT = 901
NON_MENTORED_GEN1_PCT = 46.83

MENTORING_PENERIMA_BEASISWA_PCT = 62.76
MENTORING_NON_BEASISWA_PCT = 45.12
SMD_BEASISWA = 0.3587

MENTORING_DUKUNGAN_PESERTA = 2.74
MENTORING_DUKUNGAN_NON = 2.95
SMD_DUKUNGAN_KELUARGA = -0.1932

MENTORING_KENDALA_FINANSIAL_PCT = 57.45
MENTORING_KENDALA_FINANSIAL_N = 555

# -------------------------------------------------------------------------
# 5. Nilai Tambah Terkontrol - Hero Metric (Uji V1)
# -------------------------------------------------------------------------
HERO_VALUE_ADDED_COEF = 0.0737  # +0,074 poin IPK
HERO_VALUE_ADDED_SE = 0.0096
HERO_VALUE_ADDED_CI = (0.0548, 0.0926)
HERO_VALUE_ADDED_P = r"2{,}02 \times 10^{-14}"
HERO_N = 1924

# Dekomposisi Titik Awal
BASELINE_SEM1_PESERTA = 2.6194
BASELINE_SEM1_NON = 2.6726
BASELINE_SEM1_DIFF = -0.0532

FINAL_GPA_PESERTA = 3.0058
FINAL_GPA_NON = 2.9655
FINAL_GPA_DIFF = 0.0402

RAW_DELTA_PESERTA = 0.3864
RAW_DELTA_NON = 0.2930
RAW_DELTA_DIFF = 0.0934
PCT_RAW_DELTA_LEAD = 31.88

DECOMPOSITION_BASELINE_SHARE = 56.94
DECOMPOSITION_VALUE_ADDED_SHARE = 43.06

# -------------------------------------------------------------------------
# 6. Inverse Probability Weighting (IPW) (Uji V3)
# -------------------------------------------------------------------------
IPW_ATE_DELTA = 0.0802
IPW_ATE_DELTA_CI = (0.0550, 0.1054)
IPW_ATE_DELTA_P = r"4{,}43 \times 10^{-10}"

IPW_ATE_FINAL_GPA = 0.0798
IPW_ATE_FINAL_GPA_CI = (0.0362, 0.1234)
IPW_ATE_FINAL_GPA_P = r"3{,}35 \times 10^{-4}"
POST_IPW_SMD_MAX = "< 0,06"

# -------------------------------------------------------------------------
# 7. Panel Seimbang Mahasiswa Semester 8 (Uji V2, N = 496)
# -------------------------------------------------------------------------
PANEL_N_TOTAL = 496
PANEL_PESERTA_N = 252
PANEL_NON_N = 244

PANEL_DATA = [
    {"semester": 1, "peserta": 2.7000, "non": 2.7192, "diff": -0.0192, "adj_diff": None, "p_val": None, "ci": None},
    {"semester": 2, "peserta": 3.0098, "non": 2.9935, "diff": 0.0162, "adj_diff": None, "p_val": None, "ci": None},
    {"semester": 3, "peserta": 3.2674, "non": 3.1874, "diff": 0.0800, "adj_diff": None, "p_val": None, "ci": None},
    {"semester": 4, "peserta": 3.3274, "non": 3.2282, "diff": 0.0992, "adj_diff": 0.1106, "p_val": r"3{,}99 \times 10^{-4}", "ci": (0.0494, 0.1719)},
    {"semester": 5, "peserta": 3.4061, "non": 3.2146, "diff": 0.1915, "adj_diff": None, "p_val": None, "ci": None},
    {"semester": 6, "peserta": 3.4489, "non": 3.2301, "diff": 0.2188, "adj_diff": 0.2308, "p_val": r"4{,}18 \times 10^{-14}", "ci": (0.1709, 0.2906)},
    {"semester": 7, "peserta": 3.4171, "non": 3.2368, "diff": 0.1803, "adj_diff": None, "p_val": None, "ci": None},
    {"semester": 8, "peserta": 3.4395, "non": 3.2690, "diff": 0.1705, "adj_diff": 0.1819, "p_val": r"9{,}69 \times 10^{-10}", "ci": (0.1236, 0.2402)},
]

PANEL_CUMULATIVE_SEM8_PESERTA = 3.2484
PANEL_CUMULATIVE_SEM8_NON = 3.1268
PANEL_CUMULATIVE_SEM8_DIFF = 0.1216

# -------------------------------------------------------------------------
# 8. Batas Temuan & Kesenjangan yang Belum Tertutup (Uji V7)
# -------------------------------------------------------------------------
PERSISTENT_GAP_MENTORED_VS_NONGEN1 = 0.3290  # 0,33 poin
INTERACTION_BETA = -0.0025
INTERACTION_SE = 0.0126
INTERACTION_CI = (-0.0272, 0.0222)
INTERACTION_P = 0.8444

# -------------------------------------------------------------------------
# 9. Atrisi & Status Studi (Uji V10)
# -------------------------------------------------------------------------
CORR_DELTA_DURATION = 0.4917
CORR_DELTA_P = r"< 10^{-116}"
STATUS_LULUS_PESERTA = 15.84
STATUS_LULUS_NON = 20.09
STATUS_CUTI_PESERTA = 9.09
STATUS_CUTI_NON = 4.77
STATUS_NON_AKTIF_PESERTA = 8.50
STATUS_NON_AKTIF_NON = 7.55

# -------------------------------------------------------------------------
# 10. Rekonsiliasi Definisi Kompetisi (Uji V11)
# -------------------------------------------------------------------------
TOTAL_KEGIATAN_KOMPETISI = 6414
TOTAL_KEJUARAAN_BERSIH = 4599
NON_GEN1_KEGIATAN_KOMPETISI = 5109
GEN1_KEGIATAN_KOMPETISI = 1305
GEN1_KEJUARAAN_BERSIH = 887
PARTISIPAN_NON_MEDALI = 1815

# -------------------------------------------------------------------------
# 11. Tabel Klaim yang Kami Uji dan Lepas (V1 s.d. V12)
# -------------------------------------------------------------------------
CLAIMS_EVALUATION_TABLE = [
    {
        "klaim": "Pertumbuhan laju IPK (+0,386 vs +0,293)",
        "evaluasi": "Diturunkan",
        "status": "Bertahan",
        "alasan": "Sebanyak 56,94% selisih kasar berasal dari titik awal rendah; diturunkan ke nilai tambah terkontrol +0,074 poin.",
        "kode": "V1",
    },
    {
        "klaim": "Partisipasi kompetisi internasional (6,95% vs 5,06%)",
        "evaluasi": "Melemah",
        "status": "Melemah",
        "alasan": r"Interval bootstrap memuat 1 ($p = 0{,}162$); per mahasiswa selisih lenyap pada kejuaraan bersih (2,74% vs 2,77%).",
        "kode": "V5, V9",
    },
    {
        "klaim": "Pelipatan prestasi biner umum (Has_Prestasi)",
        "evaluasi": "Gugur",
        "status": "Gugur",
        "alasan": r"Arah efek empiris terbalik: peserta lebih rendah (39,69% vs 44,73%; $\text{Adj OR} = 0{,}839$, $p = 0{,}100$).",
        "kode": "V4",
    },
    {
        "klaim": "Subkelompok irisan (Angkatan 2019, Psikologi, FK, FKM)",
        "evaluasi": "Gugur",
        "status": "Gugur",
        "alasan": r"Fluktuasi sampel kecil ($N = 39\text{--}59$); seluruh 22 irisan $p_{\text{holm}} = 1{,}0000$ setelah koreksi Holm-Bonferroni.",
        "kode": "V6",
    },
    {
        "klaim": "Penghapusan jurang kesenjangan akademik",
        "evaluasi": "Gugur",
        "status": "Batas Temuan",
        "alasan": r"Gap 0,33 poin tetap bertahan pada peserta Gen 1; interaksi $\text{Gen 1} \times \text{Pendampingan}$ tidak signifikan ($p = 0{,}844$).",
        "kode": "V7",
    },
]

# -------------------------------------------------------------------------
# 12. Ringkasan 12 Uji Ketahanan (V1 s.d. V12)
# -------------------------------------------------------------------------
ROBUSTNESS_CHECKS_SUMMARY = [
    {
        "kode": "V1",
        "fokus": "Titik Awal vs. Laju",
        "temuan": r"Dekomposisi: 56,94% selisih kasar disumbang titik awal rendah. Nilai tambah terkontrol OLS HC3: $+0{,}0737$ poin ($p = 2{,}02 \times 10^{-14}$).",
        "verdict": "Bertahan",
    },
    {
        "kode": "V2",
        "fokus": "Panel Seimbang (N = 496)",
        "temuan": r"Pola pembalikan trajektori bertahan pada orang yang sama hingga Sem 8. Keunggulan Sem 4 ($+0{,}111$), Sem 6 ($+0{,}231$), Sem 8 ($+0{,}182$), semua $p < 0{,}001$.",
        "verdict": "Bertahan",
    },
    {
        "kode": "V3",
        "fokus": "Bias Seleksi & IPW",
        "temuan": r"Ketidakseimbangan beasiswa dan ekonomi seimbang ($\text{SMD} < 0{,}06$). Estimasi IPW ATE Delta IPK tetap $+0{,}0802$ poin ($p < 10^{-9}$).",
        "verdict": "Bertahan",
    },
    {
        "kode": "V4",
        "fokus": "Prestasi Biner",
        "temuan": r"Proporsi prestasi umum peserta justru lebih rendah (39,69% vs 44,73%; $\text{Adj OR} = 0{,}839$, $p = 0{,}100$).",
        "verdict": "Gugur",
    },
    {
        "kode": "V5",
        "fokus": "Prestasi Internasional",
        "temuan": r"Rasio kegiatan $1{,}37\times$ (6,95% vs 5,06%) memiliki cluster bootstrap $95\% \text{ CI } [0{,}885; 2{,}153]$ (memuat 1, $p = 0{,}162$).",
        "verdict": "Melemah",
    },
    {
        "kode": "V6",
        "fokus": "Irisan Sampel Kecil",
        "temuan": r"Klaim Angkatan 2019, Fak. Psikologi, FK, dan FKM seluruhnya $p_{\text{holm}} = 1{,}000$ setelah koreksi Holm-Bonferroni.",
        "verdict": "Gugur",
    },
    {
        "kode": "V7",
        "fokus": "Penutupan Kesenjangan",
        "temuan": r"IPK Gen 1 peserta (3,01) tetap tertinggal 0,33 poin dari Non-Gen 1 (3,33). Interaksi tidak signifikan ($p = 0{,}844$).",
        "verdict": "Batas Temuan",
    },
    {
        "kode": "V8",
        "fokus": "Kendala & Pembanding",
        "temuan": r"Beban ganda Gen 1 (64,09%) terbukti $1{,}48\times$ lipat Non-Gen 1 (43,17%). Peserta memiliki dukungan keluarga lebih rendah (2,74 vs 2,95).",
        "verdict": "Bertahan",
    },
    {
        "kode": "V9",
        "fokus": "Definisi Prestasi Bersih",
        "temuan": r"Hanya Juara 1-3 dan Finalis: rasio internasional per mahasiswa setara (2,74% vs 2,77%, $\text{RR} = 0{,}986$, $p = 1{,}00$).",
        "verdict": "Gugur",
    },
    {
        "kode": "V10",
        "fokus": "Komposisi & Atrisi",
        "temuan": r"Delta IPK berkorelasi kuat dengan durasi semester ($r = +0{,}492$). Lulusan resmi peserta 15,84% vs 20,09% karena cuti lebih tinggi (9,09% vs 4,77%).",
        "verdict": "Bertahan",
    },
    {
        "kode": "V11",
        "fokus": "Rekonsiliasi Hitungan",
        "temuan": "Angka 5.105 terbukti salah ketik dari 5.109 (transaksi Non-Gen 1). Total transaksi mentah = 6.414, kejuaraan bersih = 4.599.",
        "verdict": "Bertahan",
    },
    {
        "kode": "V12",
        "fokus": "Reproduksi Data Mentah",
        "temuan": "Seluruh 30 angka matriks A1 s.d. F5 cocok 100% dari 5 file CSV mentah.",
        "verdict": "Bertahan",
    },
]
