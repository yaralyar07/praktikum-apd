"""
Modul Utilitas
Berisi fungsi-fungsi umum yang digunakan dalam program
"""

import os
from prettytable import PrettyTable

def bersihkan_layar():
    """Membersihkan layar console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampil_header(judul):
    """Menampilkan header dengan format tabel"""
    table = PrettyTable()
    table.field_names = [judul.upper()]
    table.align = "c"
    table.max_width = 50
    print(table)

def validasi_angka(input_str):
    """
    Validasi input angka
    Return: tuple (valid, angka)
    """
    try:
        angka = int(input_str)
        if angka < 0:
            return False, 0
        return True, angka
    except ValueError:
        return False, 0

def tampil_pesan(pesan, tipe="INFO"):
    """Menampilkan pesan dengan format tabel"""
    table = PrettyTable()
    table.field_names = [tipe]
    table.add_row([pesan])
    table.align = "l"
    print(table)
    
def input_dengan_prompt(prompt):
    """Input dengan prompt yang lebih rapi"""
    print(f">> {prompt}", end="")
    return input()

def pause():
    """Pause program sampai user menekan Enter"""
    input("\nTekan Enter untuk melanjutkan...")
