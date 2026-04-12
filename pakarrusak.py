# data rusak dan kendala nya -> "nama rusak" : {"kendala1", "kendala2", ...}
rules_rusak = {
    ("RAM Rusak", "Solusi: Coba bersihkan pin RAM dengan penghapus pensil") : {"sering_freeze", "gagal_boot", "sering_crash"},
    ("PSU Lemah", "Solusi: Coba bersihkan debu di kipas dan ventilasi PSU") : {"shutdown_random", "gagal_boot", "suara_aneh", "bau_terbakar"},
    ("Processor Overheat", "Solusi: Coba ganti thermal paste yang baru") : {"sering_freeze", "shutdown_random", "fan_kencang", "performa_turun", "layar_glitch", "cpu_panas"},
    ("Harddisk Corrupt", "Solusi: Coba ganti kabel SATA atau kabel USB") : {"sering_freeze", "suara_aneh", "performa_turun", "file_menghilang"},
    ("GPU Bermasalah", "Solusi: Coba bersihkan kipas pada GPU") : {"shutdown_random", "fan_kencang", "performa_turun", "layar_glitch", "driver_error"}
}

# array kosong menampung kendala
kendala = []

# fungsi tanya pertanyaan dan kirim ke array kendala
def tanya_kendala(kode_kendala, teks_pertanyaan):
    # menampilkan pertanyaan dan validasi
    while True:
        jawaban = input(f"{teks_pertanyaan} (y/t): ").lower()
        if jawaban in ['y', 't']:
            break
        else:
            print("Input tidak valid! Harap masukkan 'y' atau 't'\n")

    # Jika jawaban 'y', masukkan ke dalam list kendala
    if jawaban == 'y':
        kendala.append(kode_kendala)

# fungsi mendiagnosis hasil berdasarkan array kendala
def diagnosa_kendala(input_kendala):
    hasil_diagnosa = []

    for kendala, syarat_kendala in rules_rusak.items():
        # Cek apakah SEMUA gejala syarat terpenuhi oleh input user
        if syarat_kendala.issubset(input_kendala):
            hasil_diagnosa.append(kendala)

    return hasil_diagnosa if hasil_diagnosa else ["Tidak terdeteksi rusak"]

print("=== SISTEM PAKAR DIAGNOSA KERUSAKAN KOMPUTER ===")
print("Jawablah pertanyaan berikut dengan 'y' untuk Ya atau 't' untuk Tidak.\n")

# tanya kendala
tanya_kendala("sering_freeze", "Apakah layar sering freeze?")
tanya_kendala("gagal_boot", "Apakah sering gagal boot?")
tanya_kendala("sering_crash", "Apakah aplikasi sering crash saat dipakai?")
tanya_kendala("shutdown_random", "Apakah sering tiba tiba shutdown?")
tanya_kendala("suara_aneh", "Apakah ada suara aneh dari dalam komputer?")
tanya_kendala("bau_terbakar", "Apakah ada bau terbakar dari dalam komputer?")
tanya_kendala("fan_kencang", "Apakah fan berputar terlalu kencang?")
tanya_kendala("performa_turun", "Apakah ada penurunan performa yang tidak normal?")
tanya_kendala("layar_glitch", "Apakah ada glitch pada layar saat memakai komputer?")
tanya_kendala("cpu_panas", "Apakah CPU terlalu panas saat memakai komputer?")
tanya_kendala("file_menghilang", "Apakah ada beberapa file yang menghilang?")
tanya_kendala("driver_error", "Apakah muncul error driver gpu?")

# print hasil diagnosa
print(f"\nHasil Diagnosa: {diagnosa_kendala(kendala)}")