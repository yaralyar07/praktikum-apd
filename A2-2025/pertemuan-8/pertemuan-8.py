import os
import math
from math import sqrt
import random

os.system('cls' if os.name == 'nt' else 'clear')

# num = int("42") 
# name = str(123) 
# data1 = list("abc") 
# data = dict(a=1, b=2) 

# angka = 20

# buah = frozenset({"apel", "apel", "jeruk", "mangga"})
# buahset = list(buah)

# print(pow(2,3))

# buah = ["apel", "pisang", "mangga"]
# angka = 0
# for item in buah:
#     angka += 1
#     print(angka, item)

# angka = [1, 2, 3, 4, 5, 6]
# genap = filter(lambda x: x % 2 == 0, angka)
# print(list(genap))


# angka = [1, 2, 3, 4]
# kuadrat = map(lambda x: x ** 2, angka)
# print(list(kuadrat))

# angka = [10, 20, 30]
# it = iter(angka)
# print(next(it))
# print(next(it))
# print(next(it))

# huruf = "a,b,c"
# ganti = huruf.split(',')
# print(ganti)

# nama = "daFFa anak jahat"
# print(nama.lower())
# print(nama.upper())
# print(nama.strip())
# print(nama.replace('jahat','baik'))

# huruf = "a,b,c"
# print(huruf.split(","))
# print(nama.find('a'))

# pilih_acak = ["pisang", "rambutan", "manggis"]
# print(random.choice(pilih_acak))

# from datetime import datetime
# # print(datetime.now)

# import inquirer
# pertanyaan = [
#     inquirer.List(
#         "bahasa",
#         message="Kamu mau belajar bahasa apa?",
#         choices=["Python", "Java", "C++", "JavaScript"]
#     )
# ]

# jawaban = inquirer.prompt(pertanyaan)
# print("Kamu memilih:", jawaban["bahasa"])

# karakter = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+"

import sqlite3
import hashlib

def create_user_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT,
            role TEXT
        )
    ''')
    conn.commit()
    conn.close()

def register_user(username, password, role='viewer'):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                       (username, password_hash, role))
        conn.commit()
        print(f"User {username} berhasil didaftarkan.")