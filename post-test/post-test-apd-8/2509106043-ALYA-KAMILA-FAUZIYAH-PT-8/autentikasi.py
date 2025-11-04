"""
Modul Autentikasi
Menangani registrasi dan login pengguna
"""

from utils import bersihkan_layar, tampil_header, tampil_pesan, input_dengan_prompt, pause
from prettytable import PrettyTable

def register(users_data, data_keuangan):
    """
    Fungsi untuk registrasi akun baru
    Return: (success, username_baru)
    """
    bersihkan_layar()
    tampil_header("REGISTER AKUN BARU")
    print()
    
    username_baru = input_dengan_prompt("Masukkan username baru: ")
    
    if username_baru == "":
        tampil_pesan("Username tidak boleh kosong!", "ERROR")
        pause()
        return False, None
    
    if username_baru in users_data:
        tampil_pesan("Username sudah digunakan!", "ERROR")
        pause()
        return False, None
    
    password_baru = input_dengan_prompt("Masukkan password: ")
    
    if password_baru == "":
        tampil_pesan("Password tidak boleh kosong!", "ERROR")
        pause()
        return False, None
    
    konfirmasi_password = input_dengan_prompt("Konfirmasi password: ")
    
    if password_baru != konfirmasi_password:
        tampil_pesan("Password tidak cocok!", "ERROR")
        pause()
        return False, None
    
    users_data[username_baru] = password_baru
    data_keuangan[username_baru] = {}
    
    tampil_pesan(f"Akun {username_baru} berhasil dibuat!", "SUKSES")
    pause()
    return True, username_baru

def login(users_data, data_keuangan):
    """
    Fungsi untuk login
    Return: username atau None jika gagal/exit
    """
    percobaan = 0
    
    while percobaan < 3:
        bersihkan_layar()
        tampil_header("LOGIN")
        
        # Menu login
        table = PrettyTable()
        table.field_names = ["OPSI"]
        table.add_row(["Belum punya akun? Ketik 'register' pada username"])
        table.add_row(["Ingin keluar? Ketik 'exit' pada username"])
        table.align = "l"
        print(table)
        print()
        
        username = input_dengan_prompt("Username: ")
        
        if username.lower() == "register":
            success, new_user = register(users_data, data_keuangan)
            if success:
                continue
            else:
                continue
        
        if username.lower() == "exit":
            tampil_pesan("Terima kasih! Program ditutup.", "INFO")
            pause()
            return None
        
        password = input_dengan_prompt("Password: ")
        
        if username in users_data and users_data[username] == password:
            tampil_pesan(f"Login berhasil! Selamat datang, {username}!", "SUKSES")
            pause()
            return username
        else:
            percobaan += 1
            tampil_pesan(f"Username atau password salah. Percobaan {percobaan}/3", "ERROR")
            
            if percobaan >= 3:
                tampil_pesan("Terlalu banyak percobaan login. Program ditutup.", "ERROR")
                pause()
                return None
            else:
                pause()
    
    return None
