print("=" * 60)
print("             SELAMAT DATANG DI RENTAL MOBIL AI")
print("=" * 60)
print()

for i in range (0,5):
    username = (input("Username : "))
    password = (input("Password : "))
    if username == "alyar" and password == "043":
        print("\nAutentikasi berhasil")
        print()
        
        print("~" * 60)
        print()
        usia = int(input("Masukkan usia anda : "))
        if usia >= 21:
            SIM_A = input("Memiliki SIM A (ya/tidak) : ")
            if SIM_A == "ya":
                deposit = int(input("Masukkan jumlah deposit anda : "))
                if deposit >= 500000:
                    pengalaman_mengemudi = int(input("Masukkan lama pengalaman anda mengemudi (dalam tahun) : "))
                    if pengalaman_mengemudi >= 4:
                        print("\nAnda dapat melakukan perentalan untuk semua jenis mobil")
                    else:
                        print("\nAnda dapat melakukan perentalan untuk mobil standar saja")
                else:
                    print ("\nTidak dapat melakukan perentalan : Deposit anda tidak cukup")
            else:
                print("\nTidak dapat melakukan perentalan : Tidak memiliki SIM A")
        else:
            print("\nTidak dapat melakukan perentalan : Usia anda tidak mencukupi")
        
        break
    else:
        print("\nUsername atau password yang anda masukkan salah")
        print()
else:
    print("Anda telah melakukan terlalu banyak percobaan")

print()
print("=" * 60)
print("                       TERIMAKASIH")
print("=" * 60)