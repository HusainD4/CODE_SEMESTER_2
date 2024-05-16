print("===="*16)
print( "\n===========   SELAMAT DATANG DI LAYANAN KONERLING   =========== \n")
print("===="*16)
nama = str (input('nama : ')); kelas =(input('kelas : ')); jurusan = {'1': "Teknik Informatika",'2': "Ilmu Komputer",'3': "Teknik Elektro",'4': "Teknik Mesin\n"}
print("Pilih jurusan yang Anda inginkan:")
for key, value in jurusan.items():
    print(f"{key}. {value}")
pilihan = input("Masukkan nomor jurusan yang Anda pilih: ")
if pilihan in jurusan:
    print(f"Anda memilih jurusan {jurusan[pilihan]}\n")
    laporan = (input('silakan ketik apa laporan anda : '))
    print("===="*16)
    hasil = (f'Terimakasih {nama}, {kelas}, jurusan {jurusan[pilihan]}, \nlaporan anda sudah kami terima! \ntetap semangat teruslah berusaha untuk masa depan yang cerah!'); print(hasil) ; print("===="*16)
else:
    print("Pilihan tidak valid. Silakan pilih nomor jurusan yang tersedia.")











# #kriteria pekerjaan yang memenuhi syarat
# pekerjaan = ['pns','dokter','guru','TNI']

# # Menerima input dari pengguna
# nama = input("Masukkan nama mahasiswa: ")
# umur = int(input("Masukkan umur mahasiswa: "))
# pekerjaan_orang_tua = input("Masukkan pekerjaan orang tua: ")
# gaji_orang_tua = float(input("Masukkan gaji orang tua (dalam Rupiah per bulan): "))
# ipk = float(input("Masukkan IPK mahasiswa: "))

# # Untuk mengecek mahasiswa ini memenuhi kriteria atau tidak
# if (pekerjaan_orang_tua not in pekerjaan) and (gaji_orang_tua <= 1000000) and (ipk >= 2.7) and (umur < 25):

#     print("==="*20)
#     print("Nama                 :", nama)
#     print("Umur                 :", umur)
#     print("Pekerjaan Orang Tua  :", pekerjaan_orang_tua)
#     print("Gaji Orang Tua       :", gaji_orang_tua)
#     print("IPK                  :", ipk)
#     print("==="*20)
#     print("Mahasiswa memenuhi syarat untuk mendapatkan beasiswa.")
#     print("==="*20)
# else:
#     print("==="*20)
#     print("Maaf, mahasiswa tidak memenuhi syarat untuk mendapatkan beasiswa. semangat yah! jangan putus asa.")
#     print("==="*20)









# nama = str (input('masukan nama karyawan = '))
# jam_kerja = int (input('jumlah jam = '))
# tarif_perjam = int(input('tarif = '))
# jam_kerja*= 20
# hasil_gaji = jam_kerja*tarif_perjam
# print('====================================')
# print(f'jadi gaji {nama},adalah {hasil_gaji}')
# print('====================================')







# print("===="*16)
# print( "\n===========   SELAMAT DATANG DI LAYANAN KONERLING   =========== \n")
# print("===="*16)
# nama = str (input('nama : ')); kelas =(input('kelas : '))
# jurusan = {
#     '1': "Teknik Informatika",
#     '2': "Ilmu Komputer",
#     '3': "Teknik Elektro",
#     '4': "Teknik Mesin"
# }

# # Menampilkan pilihan jurusan
# print("Pilih jurusan yang Anda inginkan:")
# for key, value in jurusan.items():
#     print(f"{key}. {value}")

# # Meminta pengguna untuk memilih nomor jurusan
# pilihan = input("Masukkan nomor jurusan yang Anda pilih: ")

# # Memeriksa pilihan pengguna dan memberikan output
# if pilihan in jurusan:
#     print(f"{jurusan[pilihan]}")
#     laporan = (input('silakan ketik apa laporan anda : '))
#     hasil = (f'terimakasih{nama},{kelas},jurusan {jurusan[pilihan]}')
# else:
#     print("Pilihan tidak valid. Silakan pilih nomor jurusan yang tersedia.")




