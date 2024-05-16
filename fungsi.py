def cetak_string ():
    print('ini fungsi string')
cetak_string()


def sapaan(salam):
    print(salam)
sapaan('ini fungsi')


def penjumlahan(a,b):
    hasil = a + b
    print(hasil)
penjumlahan(5,10)


def pengurangan(a,b):
    return a - b
print(pengurangan(12,3))


def bilangan(angka):
    if angka % 2 == 0:
        return 'GENAP'
    else:
        return 'GANJIL'
print(bilangan(3))

#variabel global
nama = "pahri"
def help():
    #variabel lokal
    nama = "Husain"
    print(nama)

#akses global
print('hai namaku',nama)
help()