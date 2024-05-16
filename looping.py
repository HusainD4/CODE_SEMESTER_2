print('PENGULANGAN FOR')





#untuk memunculkan angka urutan 
for i in range(1):
    print("ayo berhitung",i)





buah = ["duren","pisang","kurma"]
nomor = [9,8,7,6,5,4]
print('\n')
for buahan in buah:
    print(buahan)

print('\n')
for index,buahan in enumerate(buah):
    print(index,buahan)
    
print('\n')
for nomors,buahan in zip(nomor,buah):
    print(nomors,buahan)

print('\n')
names = "HUSAIN MULYANSYAH"
for name in names:
    print(name)

#hanya memanggil labelnya
biodata = {'Nama\t':'HUSAIN','NIM\t':23090078}
for data in biodata:
    print(data)

#memanggil value atau isi dari label
print('\n')
for value in biodata.values():
    print(value)

print('\n')
for label,value in biodata.items():
    print(label,':',value)


print('\n')
for i in range(1,11):
    if i % 2 == 0:
        print(i,'bilangan ganji')
    else:
        print(i,'bilangan genap')
print('\n')
print('PENGULANGAN WHILE')

print('\n')
i = 1
while i <= 10:
    print(i)
    i += 1

print('\n')
i = 1
while i <= 10:
    print('mari berhitung',i)
    i += 1
print('\n')



total_ulang = 0
while True:
    main = input('ingin keluar? [Y/T]: ').lower()
    if main == 'Y' or main == 'y':
        break
    total_ulang += 1
print('total perulangan : ', total_ulang)