# Data Input
a = int(input("Harga makanan sebesar Rp "))
b = int(input("Harga snack sebesar Rp "))
c = int(input("Harga minuman sebesar Rp "))
d = int(input("Uang yang anda bawa sebesar Rp "))

# Rumus
j = int(a + b + c)
print()
print(f"Total yang harus anda bayar sebesar Rp {j}")

k = int(d - j)
# Output Akhir
if d == j :
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
elif d > j :
    print(f"Anda memiliki kembalian sebesar Rp {k}")
elif d < j :
    print(f"Uang Anda kurang! Anda memiliki utang sebesar Rp {abs(k)}")