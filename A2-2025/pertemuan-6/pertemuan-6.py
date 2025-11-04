import os

os.system('cls' if os.name == 'nt' else 'clear')
# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)

# for i in buah:
#     print (i,end= '')

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka)

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }

# print(Daftar_buku["Buku1"])
# print(Daftar_buku)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
#     "Instagram" : "daffahrhap"
#     }
# }
# print(Biodata)

# for i, j in Biodata.items():
#     print(i)
#     print(j)

# print()
# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get('pe'))

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# Film.update({"The Conjuring" : "Comedy"})
# #Setelah Ditambah
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]

# print(data)
# #memanggil data yang telah dihapus
# print(data.get("Nama"))

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][1])
# print(Musik['Paramore'][2][0])
# print(Musik ['The Chainsmoker'][0])
# print(Musik['Paramore'][2][1][0])
# print(Musik['Neffex'][1][1])

# a = {10, 11, 12}
# b = {11, 13, 14}

# c = a & b
# d = a | b
# print(c)
# print(d)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print()
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print()
# #setelah menggunakan setdefault
# print(Nilai)

