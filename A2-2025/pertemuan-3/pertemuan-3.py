angka = 5

if angka > 5:
    print("angka lebih besar dari 5")
else:
    print("angka tidak lebih besar dari 5")

cuaca = "cerah"

if cuaca == "mendung":
    print("di rumah aja")
elif cuaca == "mendung":
    print("makan mie")
else:
    print("main keluar")

nilai = 70

if nilai >= 70:
   print("anda lulus")
else:
    print("anda tidak lulus")

nilai = int(input("masukkan nilai : "))

if nilai >= 90:
    print("A")
elif nilai >= 70:
    print("B")
elif nilai >= 60:
    print("C")
else:
    print("D")

a = 4
b = 5
c = 6

if a<b:
    if a<c:
        print("a paling kecil")
    else:
        print("c lebih besar dari a")
elif a<c:
    print("c lebih besar")
else:
    print("a paling besar")