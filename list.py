person = ['dimas','husain','fahri','ihsan','iqbal','izat','akmal','evan','rifky']


person.append('ghifa')
print(person)

person.insert(1,'budi')
print(person)

person.remove('dimas')
print(person)

del person[4]
print(person)

person.pop()
print(person)

person.pop(0)
print(person)

# stack (Life in first out)
# queu (first in first out)


person1=['bagas','hilman','ihsan','akmal','izat','izat']
print(person1[3])

print(person1.index('hilman'))

print(person1.count('izat'))



my_list = ['cindy','bagas','adel','zaenal']
# mengurutkan nama
my_list.sort()
print(my_list)
# membalik data dari akhir ke awal
my_list.reverse()
print(my_list)