# membuat fungsi dengan parameter args
def kirim_sms(*nomor):
    print(nomor)

# membuat fungsi dengan parameter *kwargs
def tulis_sms(**isi):
    print(isi)

# panggil fungsi *args
kirim_sms(123, 444, 432)

# panggil fungsi *keargs
tulis_sms(tujuan=123, pesan=("apa kabar bro"))