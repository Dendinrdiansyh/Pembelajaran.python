# contoh penulisan komentar
class pagar:
    """kelas pagar untk membuat objek pagar. dibuat oleh petani kode sebagai contoh saja."""
    def __int__(self, warna, tinggi, bahan):
        self. warna = warna
        self. tinggi = tinggi
        self. bahan = bahan

# mengakses dokuemtasi kelas
print(pagar.__doc__)
input('\ntekan [enter] untuk melihat bantuan (dokumentasi) kelas: ')
help(pagar) # untuk melihat dokumentasi kelas

