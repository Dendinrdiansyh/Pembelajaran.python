# contoh 2 menampilkan semua list dimensi
list_minuman = [
    ["kopi", "susu", "es jeruk"],
    ["jus apel", "jus alpukat", " jus jeruk"],
    ["teh manis", "teh kotak", "teh tawar"]
]
for menu in list_minuman:
    for minuman in menu:
        print(minuman)