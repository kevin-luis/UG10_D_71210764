#Variabel Input
daftar = input("Masukkan daftar belanja Anda: ")
b = daftar.title().split(",")
print(f"Daftar belanja : {b}")

#Varaibel input 2
daftar2 = input("Masukkan barang yang ingin ditambahkan : ")


#Eksekusi
if daftar2 == "tOmAt":
    print(f"Barang {daftar2.upper()} sudah berada dalam daftar belanja.")

elif daftar2 != daftar :
    b.extend(daftar2.upper().split(","))
    print(f"Hasil penambahan pada daftar belanja : {b}")
