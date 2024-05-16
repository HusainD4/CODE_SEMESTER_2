def penjumlahan(a,b):
    return a + b 

def pengurangan(a,b):
    return a - b 

def pengkat(a,b):
    return a ** b

def perkalian(a,b):
    return a * b

def pembagian(a,b):
    return a / b 

def bilangan(angka):
    if angka % 2 == 0:
        return 'GENAP'
    else:
        return 'GANJIL'
    
def menu():
    print("Pilih operasi matematika:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
    return pilihan


def eksekusi():
    if menu == '1':
        hasil = penjumlahan(angka1, angka2)
        print("Hasil penjumlahan:", hasil ,"\n")
    elif menu == "2":
        hasil = pengurangan(angka1, angka2)
        print("Hasil pengurangan:", hasil ,"\n")
    elif menu == "3":
        hasil = perkalian(angka1, angka2)
        print("Hasil perkalian:", hasil ,"\n")
    else: 
        print('Selsai')
        exit()
