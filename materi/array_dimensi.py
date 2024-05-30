# deklarasi array 1D
nilai_siswa = [89,90,87,67,89,78,67,89,78,56,78,67,57]

# akses nilai array
print(nilai_siswa[1])

# Tambah data 100
nilai_siswa.append(100)
print(nilai_siswa)

# Hapus data angka 56, di dalam kurung menggunakan hitungan array
nilai_siswa.pop(9)
print(nilai_siswa)

# menghitung jumlah data
jumlah_data = len(nilai_siswa)
print(f"jumlah data : {jumlah_data}")

# menjumlahkan total yang ada di dalam array nya
total_data = sum(nilai_siswa)
print(f"total data : {total_data}")

# menghitung rata rata
rata_rata = jumlah_data / total_data
print(f"rata rata : {rata_rata}")

# memunculkan nilai tertinggi
nilai_tinggi = max(nilai_siswa)
print(f"nilai tertinggi : {nilai_tinggi}")

# memunculkan nilai terendah
nilai_rendah = min(nilai_siswa)
print(f"nilai tertinggi : {nilai_rendah}")

# ingin mengetahui jumlah nilai di atas rata rata
jumlah_nilai_diatas_rata2 = sum(True for i in nilai_siswa if i > rata_rata)
print(f"nilai diatas rata rata : {jumlah_nilai_diatas_rata2}")


# membuat data agar di urutkan dari angka 1 - terbesar
nilai_siswa.sort()
print()

# untuk membalikan data 
nilai_siswa.reverse()
print(nilai_siswa)
