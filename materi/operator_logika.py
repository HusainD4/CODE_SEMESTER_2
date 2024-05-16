
a = True
b = False

print('AND = ', a and b)
print('OR = ', a or b)
print('NOT A = ', not a)
print('NOT B = ', not b)


bayar = True
absen = int (input ("masukan nilai : "))

hasil = 'boleh ujian' if bayar == True and absen >= 70 else 'tidak boleh ujian'
print(hasil)

list1 = [1,2,3]
list2 = list1
list1.append(6)
print(list2,list2)
print(list1 is list2)