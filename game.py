# print("==="*20)
# jumlah_siswa = int(input("Masukkan jumlah siswa: "))
# print("==="*20)
# nilai_awal = 0
# for siswa in range(1, jumlah_siswa +1):
#     nilai = float(input(f"Masukkan nilai ujian siswa ke-{siswa}: "))
#     nilai_awal += nilai
# nilai_rata_rata = nilai_awal / jumlah_siswa
# print("==="*20)
# print(f"Rata-rata nilai seluruh siswa adalah: {nilai_rata_rata}")
# print("==="*20)
# n







import random

angka_acak = random.randint(1,10)
print(angka_acak)
tebak_benar = False
jumlah_tebak = 0
print("==="*20)
print('== selamat datang di Game JUHO (JUDI HOKI) ==')
print("==="*20)

while not tebak_benar:
    print("Tebak angka antara 1-10" )
    tebakan = int(input("\n==============================\nTEEBAKAN ANDA :  "))
    jumlah_tebak += 1

    if tebakan < angka_acak:
        print("===============================\nTebakan Anda kurang. Coba lagi!\n==============================")
    elif tebakan > angka_acak:
        print("==============================\nTebakan Anda berlebihan. Coba lagi!\n==============================")
    else:
        tebak_benar = True
        print(f"Selamat! Anda menebak angka dengan benar dalam {jumlah_tebak} tebakan.")




