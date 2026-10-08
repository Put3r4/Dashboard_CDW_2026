"""Kamus terstruktur seluruh teks narasi resmi Dashboard CDW 2026.

Disusun sesuai panduan penulisan ketat (Prompt_Pelatih_Menulis_Narasi.md & Prompt_Dashboard_CDW_2026.md):
- Kalimat pendek (maksimal sekitar 20 kata per kalimat)
- Satu gagasan per kalimat
- Bahasa Indonesia formal yang ringan, lugas, dan jernih
- Angka selalu disertai pembandingnya
- Menggunakan bahasa asosiasi teruji ("berasosiasi dengan", "dikaitkan dengan"), bukan sebab-akibat
- Hanya menggunakan angka resmi Tier A tervalidasi
- Nama universitas disamarkan sebagai Universitas X (data fiktif RWFD)
- Bebas dari emoji dan simbol dekoratif.
"""

CONTENT = {
    # =========================================================================
    # 1. Halaman Selamat Datang
    # =========================================================================
    "selamat_datang": {
        "hook": {
            "title": "Pesan Kunci Proyek",
            "poin_data": [
                "Nilai tambah terkontrol: +0,074 poin IPK bagi mahasiswa generasi pertama yang didampingi",
                "Kesenjangan IPK kampus: 0,35 poin antara Non-Gen 1 dan Gen 1 belum tertutup",
            ],
            "teks": (
                "Program pendampingan berasosiasi dengan nilai tambah bersih +0,074 poin IPK setelah faktor pembanding disamakan. "
                "Namun, kesenjangan IPK sebesar 0,35 poin antara mahasiswa generasi pertama dan non-generasi pertama belum tertutup."
            ),
            "pedoman": "Satu gagasan per kalimat, angka disertai pembanding, bahasa asosiasi murni.",
        },
        "perkenalan_data": {
            "title": "Perkenalan Data Universitas X",
            "poin_data": [
                "Populasi: 5.000 mahasiswa",
                "Sumber: 5 tabel data administratif dan survei institusional",
                "Sifat: Real World Fake Data (RWFD), populasi penuh (sensus)",
                "Etika: Data observasional, interpretasi berbasis asosiasi bukan sebab-akibat",
            ],
            "teks": (
                "Analisis ini mengkaji sensus penuh 5.000 mahasiswa di Universitas X dari lima tabel data institusional. "
                "Dataset ini berstatus Real World Fake Data yang dirancang menyerupai pola empiris perguruan tinggi sesungguhnya. "
                "Karena data bersifat observasional, seluruh temuan menyajikan pola asosiasi statistik tanpa klaim hubungan sebab-akibat langsung."
            ),
            "pedoman": "Transparan mengenai sifat data fiktif institusional dan prinsip kehati-hatian observasional.",
        },
        "cara_membaca": {
            "title": "Cara Membaca Dashboard Ini",
            "poin_data": [
                "Generasi Pertama (Gen 1): Mahasiswa yang orang tuanya tidak menempuh pendidikan tinggi (38,48% populasi)",
                "Program Pendampingan: Intervensi bimbingan akademik dan adaptasi kampus",
                "Nilai Tambah Terkontrol: Selisih capaian setelah menyamakan nilai awal dan karakteristik sosiodemografi",
                "Bahasa Asosiasi: Pola hubungan data observasional tanpa klaim sebab-akibat",
            ],
            "teks": (
                "Mahasiswa generasi pertama adalah pembuka jalan keluarga di perguruan tinggi dengan proporsi 38,48% populasi kampus. "
                "Nilai tambah terkontrol mengukur selisih nilai bersih setelah menyetarakan latar belakang awal mahasiswa secara adil. "
                "Seluruh hubungan disajikan dalam bahasa asosiasi karena bersumber dari data institusional observasional."
            ),
            "pedoman": "Definisi operasional baku dijelaskan secara ringkas untuk pembaca umum.",
        },
    },

    # =========================================================================
    # 2. Halaman Overview
    # =========================================================================
    "overview": {
        "ringkasan_populasi": {
            "title": "Distribusi Mahasiswa dan Lingkup Kampus",
            "poin_data": [
                "Total populasi: 5.000 mahasiswa",
                "Porsi Generasi Pertama: 38,48% (1.924 orang)",
                "Porsi Non-Generasi Pertama: 61,52% (3.076 orang)",
                "Rata-rata IPK kampus: 3,20",
                "Total catatan kompetisi: 6.414 kegiatan",
                "Tingkat keikutsertaan pendampingan pada Gen 1: 53,17% (1.023 orang)",
            ],
            "teks": (
                "Populasi Universitas X berjumlah 5.000 mahasiswa dari angkatan 2019 hingga 2025. "
                "Sebanyak 1.924 mahasiswa atau 38,48% merupakan generasi pertama, berbanding 61,52% rekan non-generasi pertama. "
                "Rata-rata IPK universitas tercatat 3,20 dari seluruh fakultas. "
                "Pangkalan data mencatat 6.414 total partisipasi kegiatan kompetisi kemahasiswaan. "
                "Sebanyak 53,17% mahasiswa generasi pertama tercatat aktif mengikuti program pendampingan kampus."
            ),
            "pedoman": "Penyajian angka demografi komparatif dengan kalimat terukur di bawah 20 kata.",
        },
        "pertanyaan_kunci": {
            "title": "Pertanyaan yang Masih Kami Cari Jawabannya",
            "items": [
                {
                    "pertanyaan": "Apakah mahasiswa generasi pertama menghadapi kendala yang lebih berat dibanding rekan lainnya?",
                    "tautan_teks": "Telusuri rincian beban di halaman Kendala →",
                    "tujuan_halaman": "3_Kendala.py",
                    "poin_data": ["Beban finansial 50,21% vs 22,17%", "Dukungan keluarga 2,84 vs 3,65"],
                    "draf": (
                        "Mahasiswa generasi pertama memikul kendala finansial 50,21%, jauh melampaui rekan non-generasi pertama di angka 22,17%. "
                        "Telusuri rincian disparitas beban ini pada halaman Kendala."
                    ),
                },
                {
                    "pertanyaan": "Siapa saja yang sebenarnya terserap ke dalam program pendampingan kampus?",
                    "tautan_teks": "Lihat profil penyerapan di halaman Insight →",
                    "tujuan_halaman": "4_Insight.py",
                    "poin_data": ["Penerima beasiswa 62,76% ikut", "Kendala finansial 57,45% ikut"],
                    "draf": (
                        "Program pendampingan menyerap 62,76% penerima beasiswa, berbanding 45,12% pada bukan penerima beasiswa. "
                        "Periksa profil kerentanan peserta pada halaman Insight."
                    ),
                },
                {
                    "pertanyaan": "Apakah pendampingan berasosiasi dengan capaian IPK yang lebih tinggi setelah faktor pembanding disamakan?",
                    "tautan_teks": "Periksa bukti nilai tambah terkontrol di halaman Insight →",
                    "tujuan_halaman": "4_Insight.py",
                    "poin_data": [r"Nilai tambah OLS HC3: $+0{,}0737$ poin ($p < 0{,}001$)", r"IPW: $+0{,}0802$ poin"],
                    "draf": (
                        "Setelah memperhitungkan seluruh faktor pembanding, peserta pendampingan membukukan keunggulan nilai bersih +0,074 poin IPK. "
                        "Buktikan hasil audit ekonometrika pada halaman Insight."
                    ),
                },
                {
                    "pertanyaan": "Apakah program pendampingan mampu menghapus kesenjangan akademik di tingkat universitas?",
                    "tautan_teks": "Evaluasi batas kesenjangan di halaman Insight →",
                    "tujuan_halaman": "4_Insight.py",
                    "poin_data": ["Kesenjangan 0,33 poin tetap bertahan", r"Interaksi: $p = 0{,}844$"],
                    "draf": (
                        "Meskipun didampingi, kesenjangan IPK sebesar 0,33 poin masih memisahkan generasi pertama dari rekan lainnya. "
                        "Evaluasi batas capaian program pada halaman Insight."
                    ),
                },
            ],
            "pedoman": "Pertanyaan pemantik tajam yang menghubungkan data deskriptif ke analisis inferensial.",
        },
    },

    # =========================================================================
    # 3. Halaman Kendala
    # =========================================================================
    "kendala": {
        "beban_finansial": {
            "title": "Kendala Finansial sebagai Beban Terbesar",
            "poin_data": [
                "Kendala finansial Gen 1: 50,21% (966 mahasiswa)",
                "Kendala finansial Non-Gen 1: 22,17% (682 mahasiswa)",
                "Perbedaan prevalensi: lebih dari 2 kali lipat",
            ],
            "teks": (
                "Sebanyak 50,21% mahasiswa generasi pertama menempatkan biaya kuliah sebagai kendala utama studi. "
                "Sebaliknya, kendala biaya hanya dialami oleh 22,17% mahasiswa non-generasi pertama. "
                "Prevalensi kendala finansial pada generasi pertama terbukti lebih dari dua kali lipat lebih tinggi."
            ),
            "pedoman": "Tekankan perbedaan proporsi dengan kalimat lugas tanpa hiperbola.",
        },
        "beban_ganda": {
            "title": "Beban Ganda Finansial dan Adaptasi",
            "poin_data": [
                "Prevalensi Gen 1: 64,09% (1.233 mahasiswa)",
                "Prevalensi Non-Gen 1: 43,17% (1.328 mahasiswa)",
                r"Rasio prevalensi (PR): $1{,}48\times$ lipat ($95\% \text{ CI } [1{,}41; 1{,}56]$, $p < 10^{-15}$)",
            ],
            "teks": (
                "Sebanyak 64,09% mahasiswa generasi pertama menanggung beban ganda finansial dan adaptasi akademik. "
                "Pada kelompok non-generasi pertama, proporsi beban serupa tercatat 43,17%. "
                "Rasio prevalensi menunjukkan risiko beban 1,48 kali lipat lebih tinggi bagi generasi pertama. "
                "Interval kepercayaan 95% terentang dari 1,41 hingga 1,56 kali lipat dengan signifikansi tinggi."
            ),
            "pedoman": "Sertakan rasio prevalensi dan interval kepercayaan secara presisi.",
        },
        "dukungan_keluarga": {
            "title": "Defisit Dukungan Edukatif Keluarga",
            "poin_data": [
                "Skor dukungan keluarga Gen 1: 2,84 dari 5,00 (standar deviasi 1,09)",
                "Skor dukungan keluarga Non-Gen 1: 3,65 dari 5,00 (standar deviasi 1,02)",
                r"Selisih rata-rata: $-0{,}81$ poin ($p < 10^{-15}$)",
                "Skor terendah pada Gen 1 berkendala finansial: 2,67 dari 5,00",
            ],
            "teks": (
                "Skor dukungan keluarga mahasiswa generasi pertama berada pada angka 2,84 dari skala 5,00. "
                "Rekan non-generasi pertama mencatatkan rata-rata 3,65 dengan selisih defisit -0,81 poin. "
                "Pada generasi pertama yang tertekan biaya, skor dukungan turun ke titik terendah 2,67. "
                "Keterbatasan modal pengalaman keluarga menuntut adanya pendampingan institusional kampus."
            ),
            "pedoman": "Hubungkan minimnya modal budaya akademik keluarga dengan perlunya dukungan kampus.",
        },
        "kesenjangan_ipk": {
            "title": "Kesenjangan IPK Tingkat Universitas",
            "poin_data": [
                "IPK rata-rata Non-Gen 1: 3,33",
                "IPK rata-rata Gen 1: 2,99",
                "Jurang kesenjangan: 0,35 poin IPK",
            ],
            "teks": (
                "Mahasiswa generasi pertama mencatatkan rata-rata IPK 2,99 di tingkat universitas. "
                "Mahasiswa non-generasi pertama membukukan rata-rata IPK 3,33 pada periode yang sama. "
                "Jurang kesenjangan akademik awal membentang sebesar 0,35 poin IPK. "
                "Ketertinggalan awal ini menjadi dasar utama perlunya intervensi terstruktur."
            ),
            "pedoman": "Sajikan selisih nilai secara objektif sebagai dasar intervensi.",
        },
        "fokus_insight_callout": {
            "title": "Fokus Insight",
            "poin_data": [
                "Program pendampingan berpotensi menjadi jembatan akselerasi",
                "Evaluasi memerlukan analisis terkontrol kovariat",
            ],
            "teks": (
                "Menghadapi beban ganda yang nyata, bagaimana program pendampingan merespons ketimpangan ini? "
                "Telusuri pembuktian nilai tambah bersih dan audit ketahanan metodologis pada halaman Insight."
            ),
            "pedoman": "Kalimat ajakan ringkas dan mengarahkan ke halaman inti.",
        },
    },

    # =========================================================================
    # 4. Halaman Insight
    # =========================================================================
    "insight": {
        "penjangkauan": {
            "title": "Profil Penyerapan Program Pendampingan",
            "poin_data": [
                "Keikutsertaan Gen 1: 53,17% (1.023 dari 1.924 orang)",
                "Penyerapan pada kendala finansial: 57,45% (555 dari 966 orang)",
                r"Penerima beasiswa yang ikut: 62,76% vs bukan beasiswa 45,12% ($\text{SMD} = +0{,}36$)",
                r"Skor dukungan keluarga peserta: 2,74 vs non-peserta 2,95 ($\text{SMD} = -0{,}19$)",
                r"IP semester 1 peserta: 2,62 vs non-peserta 2,67 (selisih $-0{,}05$ poin)",
            ],
            "teks": (
                "Program pendampingan berhasil menjangkau 53,17% mahasiswa generasi pertama di universitas. "
                "Peserta mencakup 62,76% penerima beasiswa, berbanding 45,12% pada bukan penerima beasiswa. "
                "Mahasiswa berkendala finansial terserap sebesar 57,45% ke dalam program. "
                "Dukungan keluarga peserta juga lebih rendah dengan skor 2,74 berbanding 2,95. "
                "Peserta memulai studi dengan IP semester satu lebih rendah, yaitu 2,62 berbanding 2,67. "
                "Data membuktikan program cenderung menyerap kelompok mahasiswa yang paling membutuhkan bantuan."
            ),
            "pedoman": "Gunakan istilah 'cenderung menyerap' dan tekankan pola negative selection yang positif.",
        },
        "hero_metric": {
            "title": "Nilai Tambah Terkontrol (Hero Metric)",
            "poin_data": [
                r"Koefisien regresi OLS HC3: $+0{,}0737$ poin IPK ($95\% \text{ CI } [0{,}0548; 0{,}0926]$, $p = 2{,}02 \times 10^{-14}$)",
                "Variabel kontrol: IP semester 1, angkatan, masa studi, fakultas, ekonomi, beasiswa, tempat tinggal",
                r"Dekomposisi laju kasar ($+0{,}093$ poin): 56,94% disumbang titik awal rendah, 43,06% nilai tambah akhir",
                r"Penyeimbangan IPW ATE laju IPK: $+0{,}0802$ poin ($p < 10^{-9}$)",
                r"Penyeimbangan IPW ATE IPK akhir: $+0{,}0798$ poin ($p < 0{,}001$)",
            ],
            "teks": (
                "Setelah menyamakan IP semester satu, angkatan, masa studi, fakultas, ekonomi, beasiswa, dan hunian, pendampingan berasosiasi dengan nilai tambah +0,0737 poin IPK. "
                "Estimasi ini memiliki interval kepercayaan 95% dari 0,0548 hingga 0,0926 poin. "
                "Dekomposisi data membuktikan 56,94% keunggulan laju kasar sebelumnya bersumber dari nilai awal yang tertinggal. "
                "Penyeimbangan profil melalui pembobotan kecenderungan IPW mengonfirmasi penambahan laju sebesar +0,0802 poin. "
                "Nilai tambah ini membuktikan efektivitas bimbingan setelah perbedaan latar belakang disetarakan."
            ),
            "pedoman": "Wajib cantumkan label kontrol lengkap, interval kepercayaan 95%, dan hasil IPW.",
        },
        "panel_longitudinal": {
            "title": "Lintasan Panel Mahasiswa Semester 8",
            "poin_data": [
                r"Sampel panel seimbang: $N = 496$ mahasiswa yang mencapai semester 8 (252 peserta, 244 non-peserta)",
                r"Selisih terkontrol IP semester 1: Semester 4 ($+0{,}111$), Semester 6 ($+0{,}231$), Semester 8 ($+0{,}182$), semua $p < 0{,}001$",
                r"IPK kumulatif akhir semester 8: peserta 3,25 vs non-peserta 3,13 ($+0{,}12$ poin)",
                "Catatan atrisi V10: status cuti peserta 9,09% vs non-peserta 4,77%",
                "Status kelulusan resmi: peserta 15,84% vs non-peserta 20,09%",
            ],
            "teks": (
                "Pemantauan panel seimbang melacak 496 mahasiswa yang menyelesaikan delapan semester penuh. "
                "Peserta pendampingan konsisten unggul sejak semester empat dengan keunggulan bersih +0,111 poin. "
                "Keunggulan mencapai puncak pada semester enam sebesar +0,231 poin dan bertahan di semester delapan sebesar +0,182 poin. "
                "Pada akhir semester delapan, rata-rata IPK kumulatif peserta mencapai 3,25 berbanding 3,13. "
                "Panel ini mencerminkan mahasiswa aktif tingkat akhir, bukan angka kelulusan resmi kampus. "
                "Tingkat cuti studi peserta tercatat 9,09%, berbanding 4,77% pada non-peserta."
            ),
            "pedoman": "Sertakan catatan bahwa kohor semester 8 bukan kelulusan dan sebutkan data cuti studi.",
        },
        "batas_temuan": {
            "title": "Kesenjangan Akademik yang Belum Tertutup",
            "poin_data": [
                "IPK akhir Gen 1 peserta: 3,01",
                "IPK akhir Non-Gen 1: 3,33",
                "Kesenjangan tersisa: 0,33 poin IPK",
                r"Uji interaksi $\text{Gen 1} \times \text{Pendampingan}$: $\beta = -0{,}0025$, $p = 0{,}844$",
            ],
            "teks": (
                "Rata-rata IPK akhir mahasiswa generasi pertama yang didampingi adalah 3,01. "
                "Nilai tersebut masih terpaut 0,33 poin di bawah mahasiswa non-generasi pertama sebesar 3,33. "
                "Uji interaksi regresi menghasilkan nilai p sebesar 0,844 yang tidak signifikan secara statistik. "
                "Hal ini menandakan manfaat bimbingan dirasakan serupa oleh semua kelompok mahasiswa. "
                "Program pendampingan memperkecil jarak belajar, namun belum mampu menutup kesenjangan struktural kampus."
            ),
            "pedoman": "Pengakuan jujur atas keterbatasan intervensi dalam menutup kesenjangan total.",
        },
        "kesimpulan_kotak": {
            "title": "Apa yang Bisa dan Tidak Bisa Disimpulkan",
            "poin_data": [
                r"Nilai tambah bersih teruji OLS HC3: $+0{,}0737$ poin IPK ($p < 0{,}001$)",
                "Kesenjangan sisa antargenerasi: 0,33 poin IPK",
                "Sifat inferensi: Asosiasi statistik observasional tanpa klaim kausalitas",
            ],
            "teks": (
                "Evaluasi ekonometrika membuktikan bahwa program pendampingan memberikan nilai tambah bersih teruji sebesar +0,074 poin IPK. "
                "Meski demikian, data observasional ini mencatat bahwa disparitas struktural sebesar 0,33 poin belum terhapus. "
                "Pemahaman batas metodologis ini menjadi kunci perumusan kebijakan afirmasi kampus yang objektif dan terukur."
            ),
            "bisa_disimpulkan": [
                "Pendampingan berasosiasi secara signifikan dengan nilai tambah bersih +0,074 poin IPK setelah faktor pembanding disetarakan.",
                "Program terbukti tepat sasaran menyerap mahasiswa berkendala finansial dan berdukungan keluarga rendah.",
                "Keunggulan nilai terbukti konsisten pada mahasiswa aktif yang menuntaskan delapan semester studi.",
            ],
            "tidak_bisa_disimpulkan": [
                "Data bersifat observasional sehingga hubungan yang ditemukan adalah asosiasi statistik, bukan hubungan sebab-akibat langsung.",
                "Program tidak terbukti melipatgandakan peluang raihan gelar juara pada kompetisi kemahasiswaan.",
                "Kesenjangan nilai antargenerasi belum terhapus karena jurang selisih 0,33 poin masih membentang.",
            ],
            "pedoman": "Pilah secara tegas batas metodologis sains data.",
        },
    },

    # =========================================================================
    # 5. Halaman Kesimpulan
    # =========================================================================
    "kesimpulan": {
        "tiga_temuan_inti": {
            "title": "Tiga Temuan Inti",
            "poin_data": [
                "Demografi: 38,48% generasi pertama memikul beban ganda finansial",
                r"Efektivitas: Nilai tambah terkontrol $+0{,}074$ poin IPK ($p < 0{,}001$)",
                "Batas: Jurang nilai 0,33 poin IPK tetap belum tertutup",
            ],
            "teks": (
                "Ketiga temuan ini merangkum realitas demografi, pembuktian nilai tambah, dan batas intervensi di Universitas X. "
                "Pendampingan terbukti memberi dorongan positif nyata, namun disparitas latar belakang keluarga menuntut pendekatan komprehensif."
            ),
            "items": [
                {
                    "nomor": 1,
                    "judul": "Keberadaan Demografi Nyata dan Rentan",
                    "poin_data": ["38,48% mahasiswa (1.924 orang)", r"Beban ganda finansial 64,09% ($PR = 1{,}48\times$)"],
                    "draf": (
                        "Generasi pertama mencakup 38,48% populasi kampus dan menanggung beban ganda finansial 1,48 kali lipat lebih tinggi."
                    ),
                },
                {
                    "nomor": 2,
                    "judul": "Nilai Tambah Bersih yang Konsisten",
                    "poin_data": [r"$+0{,}074$ poin IPK terkontrol ($p < 0{,}001$)", r"IPW $+0{,}080$ poin", r"Panel Sem 6 $+0{,}231$ poin"],
                    "draf": (
                        "Pendampingan berasosiasi dengan nilai tambah terkontrol +0,074 poin IPK yang terbukti konsisten pada panel semester delapan."
                    ),
                },
                {
                    "nomor": 3,
                    "judul": "Kesenjangan Struktural yang Belum Tuntas",
                    "poin_data": ["Gap IPK 0,35 poin umum", "Gap 0,33 poin pada peserta pendampingan"],
                    "draf": (
                        "Kesenjangan IPK sebesar 0,33 poin belum tertutup, menegaskan perlunya integrasi bimbingan akademik dengan bantuan finansial."
                    ),
                },
            ],
            "pedoman": "Tiga pesan kunci eksekutif bagi pimpinan kampus.",
        },
        "angka_sorotan": {
            "title": "Angka Sorotan Utama",
            "angka": "+0,074 Poin IPK",
            "label_kontrol": "Setelah menyamakan IP semester 1, angkatan, masa studi, fakultas, kondisi ekonomi, beasiswa, dan tempat tinggal",
            "poin_data": [
                r"Model OLS HC3: koefisien $+0{,}0737$ poin IPK ($p = 2{,}02 \times 10^{-14}$)",
                r"Interval kepercayaan $95\%$: $[0{,}0548; 0{,}0926]$",
                r"Pembobotan IPW ATE: $+0{,}0802$ poin laju pertumbuhan IPK",
            ],
            "teks": (
                "Nilai tambah bersih +0,074 poin IPK membuktikan peran nyata intervensi pendampingan bagi mahasiswa generasi pertama. "
                "Capaian teruji ini menjadi bukti empiris efektivitas program bimbingan belajar di tingkat universitas."
            ),
            "pedoman": "Sertakan label kontrol kovariat ketat.",
        },
        "rekomendasi": {
            "title": "Usulan Rekomendasi Kebijakan Kampus",
            "poin_data": [
                "Prioritas 1: Kemitraan beasiswa dan bimbingan belajar wajib",
                "Prioritas 2: Modul adaptasi belajar intensif semester satu",
                "Prioritas 3: Layanan konseling dini guna menekan angka cuti studi",
            ],
            "teks": (
                "Rekomendasi kebijakan ini dirancang agar intervensi akademik bersinergi dengan penopang finansial mahasiswa. "
                "Pendampingan harus diperkuat sejak semester pertama sebelum ketertinggalan kumulatif terbentuk. "
                "Sistem pendampingan juga wajib memitigasi risiko atrisi agar mahasiswa dapat menyelesaikan studi tepat waktu."
            ),
            "items": [
                {
                    "rekomendasi": "Integrasi Program Beasiswa dan Mentoring Terstruktur",
                    "poin_data": ["50,21% berkendala finansial", "62,76% penerima beasiswa ikut pendampingan"],
                    "draf": (
                        "Sebanyak 50,21% mahasiswa generasi pertama menghadapi kendala biaya, namun 62,76% penerima beasiswa aktif mengikuti bimbingan. "
                        "Universitas disarankan mewajibkan skema pendampingan akademik bagi seluruh penerima bantuan finansial."
                    ),
                },
                {
                    "rekomendasi": "Intervensi Adaptasi Dini pada Semester Pertama",
                    "poin_data": ["Baseline IP Sem 1 peserta 2,62 vs 2,67", "Crossover baru terjadi di Semester 3"],
                    "draf": (
                        "Titik temu keunggulan baru terjadi pada semester tiga setelah ketertinggalan nilai awal semester satu. "
                        "Kampus perlu memperkuat modul adaptasi belajar sejak semester awal guna mempercepat fase adaptasi."
                    ),
                },
                {
                    "rekomendasi": "Mitigasi Risiko Atrisi dan Fleksibilitas Masa Studi",
                    "poin_data": ["Tingkat cuti peserta 9,09% vs non-peserta 4,77%"],
                    "draf": (
                        "Tingkat cuti kuliah peserta tercatat 9,09% berbanding 4,77% pada rekan non-peserta. "
                        "Universitas perlu menyediakan layanan konseling dan fleksibilitas kurikulum untuk menekan angka cuti studi."
                    ),
                },
            ],
            "pedoman": "Tiga rekomendasi yang aplikatif dan berbasis bukti.",
        },
    },

    # =========================================================================
    # 6. Halaman Reference
    # =========================================================================
    "reference": {
        "teknologi": {
            "title": "Spesifikasi Teknologi dan Pustaka",
            "python_version": "Python 3.10+",
            "dashboard_stack": [
                {"pustaka": "streamlit", "versi": "1.51.0", "peran": "Kerangka kerja antarmuka web interaktif"},
                {"pustaka": "pandas", "versi": "2.x", "peran": "Manipulasi dan agregasi dataset tabular"},
                {"pustaka": "plotly", "versi": "6.x / 5.x", "peran": "Visualisasi grafik interaktif responsif"},
                {"pustaka": "numpy", "versi": "1.26+ / 2.x", "peran": "Operasi komputasi numerik"},
            ],
            "analysis_stack": [
                {"pustaka": "statsmodels", "versi": "0.14.5", "peran": "Regresi OLS dengan galat baku robust HC3"},
                {"pustaka": "scikit-learn", "versi": "1.7.2", "peran": "Estimasi Propensity Score untuk bobot IPW"},
                {"pustaka": "scipy", "versi": "1.16+", "peran": "Uji hipotesis statistik dan Fisher Exact Test"},
            ],
            "pedoman": "Sajikan stack teknologi secara transparan dan terinci.",
        },
        "pipeline_notebook": {
            "title": "Alur Pipeline Analisis Data",
            "items": [
                {"notebook": "01_load_and_merge.ipynb", "tahap": "Ingestion & Merging", "keluaran": "Validasi relasional 5 CSV dan master mentah"},
                {"notebook": "02_cleaning_preprocessing.ipynb", "tahap": "Cleaning & Feature Engineering", "keluaran": "Pembersihan spasi, rentang nilai, Delta IPK kumulatif"},
                {"notebook": "03_eda.ipynb", "tahap": "Exploratory Data Analysis", "keluaran": "12 tabel agregasi Single Source of Truth"},
                {"notebook": "04_insight_summary.ipynb", "tahap": "Synthesis & Storytelling", "keluaran": "Matriks insight acuan poster dan dashboard"},
                {"notebook": "05_validasi_skeptis.ipynb", "tahap": "Robustness Checks (V1-V12)", "keluaran": "Audit empiris OLS HC3, IPW, panel seimbang, bootstrap, Holm"},
            ],
            "pedoman": "Dokumentasikan tahapan pipeline secara kronologis.",
        },
        "etika_dan_reproduksi": {
            "title": "Catatan Etika, Sifat Data, dan Reproduksibilitas",
            "poin_data": [
                "Dataset bersifat observasional dan fiktif (Real World Fake Data)",
                "Nama universitas disamarkan menjadi Universitas X",
                "Replikasi deterministik dengan seed tetap (seed = 42)",
                "Kode dan dataset terbuka untuk diaudit secara mandiri",
            ],
            "teks": (
                "Dataset kompetisi berstatus Real World Fake Data institusional Universitas X dengan sensus 5.000 mahasiswa. "
                "Seluruh temuan menyajikan pola asosiasi data observasional dan tidak boleh ditafsirkan sebagai klaim kausal langsung. "
                "Pengujian ekonometrika bersifat deterministik dan dapat direproduksi menggunakan seed 42 pada notebook lima."
            ),
            "pedoman": "Jaga kepatuhan etika data dan anonimitas institusi.",
        },
    },
}
