#input Def

#Angka Terbesar
def terbesar(a, b, c) :
    if a > b and a > c :
        return a
    elif b > a and b > c :
        return b
    else :
        return c

#Angka Tengah
def tengah(a, b, c) :
    if (b > a > c) or (c > a > b) :
        return a
    elif (a > b > c) or (c > b > a) :
        return b
    else :
        return c

#Angka Terkecil
def terkecil(a, b, c) :
    if a < b and a < c :
        return a
    elif b < a and b < c :
        return b
    else : 
        return c

#Variabel Input
a = int(input("Masukkan bilangan 1 : "))
b = int(input("Masukkan bilangan 2 : "))
c = int(input("Masukkan bilangan 3 : "))

#Variabel Output
b1 = terbesar(a, b, c)
b2 = tengah(a, b, c)
b3 = terkecil(a, b, c)

print(f"Urutan bilangan dari yang terbesar adalah {b1} {b2} {b3}")
 