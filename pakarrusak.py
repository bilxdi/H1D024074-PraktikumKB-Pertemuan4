# data rusak dan kendala nya -> "nama rusak" : "kendala1", "kendala2", ...
rules_rusak = {
    "RAM Rusak" : {"sering_freeze", "gagal_boot", "sering_crash"},
    "PSU Lemah" : {"shutdown_random", "gagal_boot", "suara_aneh", "bau_terbakar"},
    "Processor Overheat" : {"sering_freeze", "shutdown_random", "fan_kencang", "performa_turun", "layar_glitch"},
    "Harddisk Corrupt" : {"sering_freeze", "suara_aneh", "performa_turun", "file_tidak_terbuka"},
    "GPU Bermasalah" : {"sering_freeze", "shutdown_random", "demam", "mimisan", "mual"}
}

semua_kendala = [
    ("nyeri_otot", "Apakah Anda merasa nyeri otot?"),
    ("muntah", "Apakah Anda muntah muntah?"),
    ("kejang", "Apakah Anda mengalami kejang kejang?"),
    ("menggigil", "Apakah Anda sering menggigil?"),
    ("tidak_enak_badan", "Apakah Anda merasa tidak enak badan?"),
    ("keringat_dingin", "Apakah Anda keluar keringat dingin?"),
    ("sakit_kepala", "Apakah Anda merasa sakit kepala?"),
    ("mimisan", "Apakah Anda mengalami mimisan?"),
    ("mual", "Apakah Anda merasa mual?"),
    ("demam", "Apakah Anda mengalami demam?")
]

def diagnosa_malaria(gejala_input):
    hasil_diagnosa = []

    for penyakit, gejala_syarat in rules_rusak.items():
        # Cek apakah SEMUA gejala syarat terpenuhi oleh input user
        if gejala_syarat.issubset(gejala_input):
            hasil_diagnosa.append(penyakit)

    return hasil_diagnosa if hasil_diagnosa else ["Tidak terdeteksi penyakit"]

# Simulasi seperti perintah assertz di Prolog
gejala_pasien = {"nyeri_otot", "menggigil", "tidak_enak_badan"}
print(f"Hasil Diagnosa: {diagnosa_malaria(gejala_pasien)}")