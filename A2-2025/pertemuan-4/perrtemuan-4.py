# for i in range(10):
#     print(i + 1)

# print()

# for i in range(1, 11):
#     print(i)

# nama = ['alyar', 'jikra', 'athia', 'jakiya']
# for i in nama:
#     print(i)

# for i in range(10):
#     print('alpro')

# jawab = 'ya'
# hitung = 0

# while (jawab == 'ya'):
#     hitung += 1
#     jawab = input("ulang lagi? ")

# print(f"total jawab ya {hitung}")

# cuaca = 'hujan'

# while (cuaca == 'hujan' or cuaca == 'Hujan'):
#     print("jangan keluar rumah")
#     cuaca = input("Apa cuaca saat ini? ")
# print('pergi keluar rumah')

# angka = 10

# while (angka > 1):
#     print(angka)
#     angka -= 2

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i * j}")
#     print()

# angka = [2, 5, 6, 8, 16, 20, 17]

# print("mencari angka yang lebih besar dari 10....")
# print()

# for i in angka:
#     print(f"memeriksa angka {i}")
#     if i > 10:
#         print(f"{i} lebih besar dari 10")
#         break
#     print(f"angka {i} dieliminasi")
#     print()

# print()
# print("program selesai")

# n = int(input("sejauh mana anda ingin mencari angka genap? "))
# print()

# for i in range(1,n + 1):
#     if i % 2 != 0:
#         continue
#     print(f"angka genap ditemukan yaitu : {i}")
#     print("-" * 32)

# print()
# print("program selesai")

# x = int(input("batas awal : "))
# n = int(input("batas akhir : "))
# kuadrat = [i**2 for i in range(x,n + 1)]
# print(kuadrat)

# for i in range(1,6):
#     print(1**2)

# angka_ganjil = [i for i in range(1,11) if i % 2 != 0]
# print(angka_ganjil)

for i in range(1,6):
    print("*" * i)
print()

for i in range(1,6):
    print("*" * (6 - i))
print()

for i in range(1,6):
    print("*" * i )