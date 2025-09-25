# studi kasus 1
# tinggi = int(input("masukkan tinggi badan : "))

# status = "boleh naik wahana" if tinggi >= 145 else "tidak boleh naik wahana"
# print(status)

# harga = int(input("masukkan total belanja : "))

# studi kasus 2
# if harga > 100000:
#     print("dapat diskon 20%")
#     bayar = harga * 0.8
#     print("harga yang dibayar : Rp. " + str(bayar))
# elif harga > 50000:
#     print("dapat diskon 10%")
#     bayar = harga * 0.9
#     print("harga yang dibayar : Rp. " + str(bayar))
# else:
#     print("tidak dapat diskon")

nilai = int(input("masukkan nilai : "))
kelas = input("masukkan kelas : ")

if nilai >= 80 and kelas == "A":
    print("IPK 4")
elif nilai >= 80 and kelas == "B":
    print("IPK 3")
else:
    print("IPK 2")

