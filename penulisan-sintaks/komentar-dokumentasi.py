class pagar:
    """ kelas pagar untuk membuat objek pagar. dibuat oleh petani kode sebagai contoh saja."""
    def __init__(self, warna, tinggi, bahan) :
        self.warna = warna 
        self.tinggi = tinggi
        self.bahan = bahan
        
# mengakses dokumentasi kelas
print(pagar.__doc__)
input('\ntekan [enter] untuk membatu melihat (dokumentasi) kelas: ')
help(pagar)
