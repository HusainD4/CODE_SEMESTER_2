import numpy as np

# array 1 dimensi
array1 = np.array([160,120,130,170,140])
print(array1)

# # array 1 dimensi
# array1 = np.array([
#     [160,120,130,170,140]
#     [160,120,130,170,140]
#     [160,120,130,170,140]
# ])
# print(array1)

# untuk menghitung nilai rata rata
rata_rata = np.mean(array1)
print(rata_rata)

# menampikan nilai tengah atau median
print(np.median(array1))

# untuk menampilkn nilai tertinggi
print(np.max(array1))

# untuk menampilkan nilai terendah
print(np.min(array1))


# untuk nilai di atas rata rata ada berapa
print(np.sum(array1 > rata_rata))
