
stok_barang = {}

def tambah_barang():
    print("---------------------------------")
    nama_barang = input("Masukkan nama barang: ")
    jumlah_stok = int(input("Masukkan jumlah stok: "))
    print("---------------------------------")
    
    if nama_barang in stok_barang:
        stok_barang[nama_barang] += jumlah_stok
    else:
        stok_barang[nama_barang] = jumlah_stok
    print(f"- {nama_barang} stok {jumlah_stok} telah ditambahkan.\n")
    print("---------------------------------")

def hapus_barang():
    

def tampilkan_barang():
    if stok_barang:
        print("---------------------------------")
        print("---DATA BARANG---")
        for nama_barang, jumlah_stok in stok_barang.items():
            print(f"- {nama_barang}      \t Stok \t: {jumlah_stok}")
        print()
    else:
        print("---------------------------------")
        print("Tidak ada data barang dalam sistem.")
        print("---------------------------------\n")

def main():
    print("---------------------------------")
    print("selamat datang di program management stock barang!\n")
    while True:
        print("---------------------------------")
        print("silakan pilih menu : ")
        print("---------------------------------")
        print("1. Tambah Data Barang")
        print("2. Hapus Data Barang")
        print("3. Tampilkan Data Barang")
        print("4. Keluar")
        print("---------------------------------")
        
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program manajemen stok barang.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")
main()