import os

os.system('cls' if os.name == 'nt' else 'clear')

# def perkenalan():
#     print("Halo, aku Nabil")
      
# perkenalan()

# def salam():
#   print ("Halo, Ridho")
# def kali():
#   X = 5*5
#   print(X)

# salam()
# salam()
# salam()
# kali()
# kali()
# kali()

# def nama_fungsi(parameter):
#   print(parameter)

# nama_fungsi("Selamat Pagi")

# def luas_persegi_panjang(panjang, lebar):
#   luas = panjang * lebar
#   print ("luas persegi panjang adalah ", luas)

# luas_persegi_panjang(4, 5)

# def luas_persegi(sisi):
#   luas = sisi * sisi
#   return luas

# # pemanggilan fungsi luas persegi
# print ("Luas persegi :", luas_persegi(8))

# # rumus: sisi x sisi
# def luas_persegi(sisi):
#   luas = sisi * sisi
#   return luas
# # rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#   volume = luas_persegi(sisi) * sisi
#   print ("Volume Persegi = ", volume)

# # pemanggilan Fungsi
# luas_persegi(4)
# volume_persegi(6)

# def luas_segitiga(alas,tinggi):
#   luas = 0.5 * alas * tinggi
#   return int(luas)

# alas = int(input("masukkan alas : "))
# tinggi = int(input("masukkan tinggi : "))
# print("luas segitiga : ", luas_segitiga(alas,tinggi)) 

# def faktorial(n):
#   if n == 1 or n == 0:
#     return 1
# # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#   else:
#     return n * faktorial(n - 1)
    
# hasil = faktorial(5)
# print(f"Hasil dari 5! adalah: {hasil}")

# film = []


# def show_data():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     if len(film) <= 0:
#         print("Belum Ada data")
#     else:
#         print("ID | Judul Film")
#         for indeks in range(len(film)):
#             print(indeks, "|", film[indeks])

# # Fungsi untuk menambah data
# def insert_data():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     film_baru = input("Judul Film: ")
#     film.append(film_baru)
#     print("Film berhasil ditambahkan!")


# # Fungsi untuk mengedit data
# def edit_data():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         film[indeks] = judul_baru
#         print("Film berhasil diupdate!")


# # Fungsi untuk menghapus data
# def delete_data():
#     os.system('cls' if os.name == 'nt' else 'clear')
#     show_data()
#     indeks = int(input("Inputkan ID film: "))
#     if indeks >= len(film) or indeks < 0:
#         print("ID salah")
#     else:
#         film.remove(film[indeks])
#         print("Film berhasil dihapus!")


# # fungsi untuk menampilkan menu
# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")

#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# while True:
#   show_menu()

# try:
#   angka = int(input('Masukkan Angka : '))
# except ValueError:
#   print('input yang anda masukkan bukan Integer (angka)')

while True:
  try:
    nama = input("masukkan nama anda: ")
    if nama == "" or nama == " ":
      raise ValueError("nama tidak boleh kosong")
    else:
      break
  except ValueError as e:
    print (e)
  