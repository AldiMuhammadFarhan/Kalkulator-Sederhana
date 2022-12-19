''' Aplikasi Kalkulator sederhana '''

# Tambah


def tambah(x, y):
    return x+y

# Kurang


def kurang(x, y):
    return x-y

# kali


def kali(x, y):
    return x*y

# bagi


def bagi(x, y):
    return x/y

# Input pilihan
print("Kalkulator Sederhana: ")
print("1. Jumlah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
pilih = input("Pilihan saya: ")

# Input angka
px = int(input("Masukkan Bilangan: "))
py = int(input("Masukkan Bilangan: "))

# If Else
if pilih == '1':
    print(px, " + ", py, " = ", tambah(px, py))

elif pilih == '2':
    print(px, " - ", py, " = ", kurang(px, py))

elif pilih == '3':
    print(px, " x ", py, " = ", kali(px, py))

elif pilih == '4':
    print(px, " : ", py, " = ", bagi(px, py))

else:
    print("Gagal")
