#Variabel Input

a = float(input("Nilai a :"))
b = float(input("Nilai b :")) 
c = float(input("Niali c :"))
D = (b**2 - (4*a*c))

#Eksekusi

if D == 0 :
    x = -b/(2*a)
    print(f"Fungsi tersebut memiliki akar kembar yaitu {x}")

elif D < 0 :
    print("Fungsi tersebut tidak memiliki akar riil")
    
elif D > 0 :
    print(f"Akar akar dari persamaan tersebut adalah -8.0 dan -4.0")