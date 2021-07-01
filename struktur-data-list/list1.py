# membuat list yang kosong untuk menampung hobi
hobi = []
stop = False
i = 0

# mengisi hobi
while(not stop):
    hobi_baru = input("inputkan hobi yang ke-{} :". format(i))
    hobi.append(hobi_baru)
    
    # increment i
    i += 1
    tanya = input("mau isi lagi? (ya\tidak): ")
    if(tanya == "t"):
        stop = True
    
    # cetak semua hobi
    print("hobi")
    print("kamu meiliki {} hobi". format(len(hobi)))
    for hb in hobi:
        print("-{}". format(hb))
    