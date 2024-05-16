
nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (Design/Programmer/Resource): ")
status_perkawinan = input("Masukkan status perkawinan (Y/T): ")

if jabatan == "Design":
    gaji_pokok = 5000000
elif jabatan == "Programmer":
    gaji_pokok = 10000000
elif jabatan == "Resource":
    gaji_pokok = 5000000
else:
    print("Jabatan tidak valid")
    exit()

if status_perkawinan == "Y":
    tunjangan_keluarga = 0.2 * gaji_pokok
else:
    tunjangan_keluarga = 0


gaji_kotor = gaji_pokok + tunjangan_keluarga
pajak = 0.1 * gaji_kotor
total_pendapatan = gaji_kotor - pajak

print("Nama Karyawan:", nama)
print("Jabatan:", jabatan)
print("Gaji Pokok:", gaji_pokok)

if status_perkawinan == "Y":
    print("Tunjangan Keluarga:", tunjangan_keluarga)
print("Gaji Kotor = Rp.{gaji_kotor:,.0f}")
print("Pajak:", pajak)
print(f"Total gaji = Rp.{total_pendapatan:,.0f}")