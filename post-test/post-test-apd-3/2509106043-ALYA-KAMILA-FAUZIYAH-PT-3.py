print("=" * 60)
print("             SELAMAT DATANG DI RENTAL MOBIL AI")
print("=" * 60)
print()

usia = int(input("Masukkan usia anda : "))
if usia >= 21:
    SIM_A = input("Memiliki SIM A (ya/tidak) : ")
    if SIM_A == "ya":
        deposit = int(input("Masukkan jumlah deposit anda : "))
        if deposit >= 500000:
            pengalaman_mengemudi = int(input("Masukkan lama pengalaman anda mengemudi (dalam tahun) : "))
            if pengalaman_mengemudi >= 4:
                print()
                print("Anda dapat melakukan perentalan untuk semua jenis mobil")
            else:
                print()
                print("Anda dapat melakukan perentalan untuk mobil standar saja")
        else:
            print()
            print ("Tidak dapat melakukan perentalan : Deposit anda tidak cukup")
    else:
        print()
        print("Tidak dapat melakukan perentalan : Tidak memiliki SIM A")
else:
    print()
    print("Tidak dapat melakukan perentalan : Usia anda tidak mencukupi")

print()
print("=" * 60)
print("                       TERIMAKASIH")
print("=" * 60)