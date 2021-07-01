class pagar:
    """ kelas pagar untuk membuat obejek pagar. dibuat oelh petani kode sebagai contoh saja."""
    def __init__(self, warna, tinggi, bahan) :
        self.warna = warna
        self.tinggi = tinggi
        self.bahan = bahan
        
# Mengakses dokumentasi kelas
print(pagar.__doc__)
input('\ntekan [enter] untuk melihat bantuan (dokumentasi) kelas: ')
help(pagar) # untuk melihat dokumentasi kelas

