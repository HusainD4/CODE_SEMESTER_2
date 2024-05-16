#penggabungan
string1 = 'hello'
string2 = 'world!'
print(string1 +' ' + string2)
print((string1 +' ' + string2)*20)

data_kalimat = ['aku','adalah','mahasiswa']
kalimat = ' '.join(data_kalimat)
print(kalimat)

data_kalimat1 = 'jurusanku adalah informatika, bisa di sebut dengan programer'
pisah = data_kalimat1.split()
print(pisah)

substring = data_kalimat1.replace('programer','design')
print(substring)
print(data_kalimat1[0:28])


#ubah format nama
nama = 'Husain mUlyansyah'
print(nama.lower())
print(nama.upper())
print(nama.capitalize())
print(nama.title())


#matauang
harga = 15000000000000
harga = 15000000000000
print('{:,}'.format(harga))
print('{:.2f}'.format(harga))
print('{:,.2f}'.format(harga))
print(f'{harga:,}')