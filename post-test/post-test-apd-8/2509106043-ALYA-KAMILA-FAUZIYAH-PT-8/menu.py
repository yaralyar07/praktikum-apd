"""
Modul Menu
Menangani tampilan dan navigasi menu utama
"""

from utils import bersihkan_layar, tampil_header, tampil_pesan, input_dengan_prompt, pause
from transaksi import cek_saldo, catat_pemasukan, catat_pengeluaran, hapus_data
from prettytable import PrettyTable

def menu_utama(current_user, data_keuangan):
    """Menampilkan dan menangani menu utama"""
    while True:
        bersihkan_layar()
        tampil_header("PROGRAM PENCATAT KEUANGAN")
        
        # Tampilkan info user
        table_user = PrettyTable()
        table_user.field_names = ["USER AKTIF"]
        table_user.add_row([current_user])
        table_user.align = "c"
        print(table_user)
        print()
        
        # Menu utama
        print("MENU UTAMA:")
        table_menu = PrettyTable()
        table_menu.field_names = ["NO", "MENU"]
        table_menu.add_row(["1", "Cek Sisa Tabungan"])
        table_menu.add_row(["2", "Catat Pemasukan"])
        table_menu.add_row(["3", "Catat Pengeluaran"])
        table_menu.add_row(["4", "Hapus Data Tabungan"])
        table_menu.add_row(["5", "Logout"])
        table_menu.align["NO"] = "c"
        table_menu.align["MENU"] = "l"
        print(table_menu)
        print()
        
        pilihan = input_dengan_prompt("Pilih menu (1-5): ")
        
        if pilihan == "1":
            cek_saldo(current_user, data_keuangan)
        elif pilihan == "2":
            catat_pemasukan(current_user, data_keuangan)
        elif pilihan == "3":
            catat_pengeluaran(current_user, data_keuangan)
        elif pilihan == "4":
            if hapus_data(current_user, data_keuangan):
                break
        elif pilihan == "5":
            tampil_pesan("Logout berhasil!", "SUKSES")
            pause()
            break
        else:
            tampil_pesan("Pilihan tidak valid! Masukkan angka 1-5.", "ERROR")
            pause()
