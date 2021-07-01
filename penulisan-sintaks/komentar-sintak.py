# contoh 1
# ini adalah komentar
# ini juga adalah komentar

# contoh 2
" ini adalah komentar dengan tanda petik ganda"
'ini adalah komentar dengan tanda petik tunggal'

# contoh 3
class pagar :
    """kelas pagar dibuat untuk obejek pagar. dibuat oleh petani kode sebagai contoh saja."""
    def __init__(self, warna, tinggi, bahan):
        self.warna = warna
        self.tinggi = tinggi
        self.bahan = bahan
        
# mengakses dokumentasi
print(pagar. __doc__)
input('\ntekan [enter] untuk melihat bantuan (dokumetasi) kelas: ')
help(pagar) # untuk melihat dokumetasi kelas