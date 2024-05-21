# Inisialisasi data barang
barang = []

# Fungsi untuk menambahkan barang ke dalam list barang
def tambah():
    nama = input('Masukan Nama Barang : ')
    stok = input('Masukan Stok Barang : ')
    data_baru = {'nama barang': nama, 'stok': stok}
    barang.append(data_baru)

# Fungsi untuk menampilkan data barang
def tampilkan_data_barang():
    print("= = = = = T o k o E l e k t r o n i k = = = = =")
    if barang:
        print("= = = = = = D a t a B a r a n g = = = = = =")
        for item in barang:
            print(f"- {item['nama barang']} stock {item['stok']}")
    else:
        print("- - - - D a t a B a r a n g K o s o n g - - - -")

# Fungsi untuk mencari data barang berdasarkan nama
def cari_data():
    if barang:
        kata = input("Cari Nama Barang: ")
        ditemukan = False
        for item in barang:
            if kata.lower() in item['nama barang'].lower():
                print("=== HASIL PENCARIAN ===")
                print(f"- {item['nama barang']} stock {item['stok']}")
                ditemukan = True
        if not ditemukan:
            print("Barang tidak ditemukan.")
    else:
        print("- - - - D a t a B a r a n g K o s o n g - - - -")


# Menu utama program
def main():
    while True:
        print("\nP i l i h a n :")
        print("1 . T a m b a h D a t a B a r a n g")
        print("2 . E d i t D a t a")
        print("3 . H a p u s D a t a B a r a n g")
        print("4 . C a r i D a t a")
        print("5 . T a m p i l k a n D a t a B a r a n g")
        print("6 . T a m p i l k a n J u m l a h D a t a")
        print("7 . K e l u a r")

        pilihan = int(input("Masukkan pilihan : "))

        if pilihan == 1:
            tambah()
        if pilihan == 4:
            cari_data()
        if pilihan == 5:
            tampilkan_data_barang()
        if pilihan == 7:
            print("Terima kasih!")
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-7.")

# Panggil fungsi main untuk memulai program
main()
