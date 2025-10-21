# matakuliah = ['APD', 'ORSIKOM', 'kalkulus']

# print(matakuliah[-4])

# matakuliah.append('matdis')

# print(matakuliah)

# praktikum = ['mahasiswa', 'true', '133', '45.10', ['APD', 'list']]

# print(praktikum)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']

# del matakuliah[2]
# matakuliah.remove('PTI')

# print(matakuliah)

# list = [1, 2, 3]

# print(len(list))
# print(sum(list))
# print(min(list))
# print(max(list))
# print(sum(list)/len(list))

# list = [1,2,3]
# nilai = [4,5,6]

# hasil = list + nilai
# print(hasil)

# matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris', 'Orsikom','Basis Data']

# for i in matakuliah:
#     print(f"matakuliah {i}")

# for index,i in enumerate(matakuliah):
#     print(index,i)

# kelas = [
#     ["Ridho", "Lian", "Nabil"],
#     ["Daffa", "Dante", "Santoso"],
#     ["Pernanda", "Riyadi", "Ahnaf"]
#     ]

# kelas[1].insert(1,'rafi')

# print(kelas[1])
# print(kelas[0][2])
# print(kelas[2])
# print(kelas[2][0])\

# for i in kelas:
#     for j in i:
#         print(j)

# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))

# print(anggota)

studyclub = ("Data Science", "Robotics", "Multimedia", "Network")

liststudy = list(studyclub)

liststudy.append("Web")

studyclub = tuple(liststudy)

# print(studyclub)
print(f"ini list : {liststudy}")
print(f"ini tuple : {studyclub}")
