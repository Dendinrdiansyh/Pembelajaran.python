# membuat fungsi parameter dengan *args
def kirim_pesan(*nomor):
    print(nomor)
    
# membuat fungsi parameter dengan *kwargs
def tulis_sms(**isi):
    print(isi)
    
# panggil fungsi args
kirim_pesan(123,432,442)

# panggil fungsi kwargs
tulis_sms(tujuan= 123, pesan= "apakah kamu baik-baik saja?")