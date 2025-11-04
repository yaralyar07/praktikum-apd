"""
Modul Transaksi
Menangani operasi keuangan (pemasukan, pengeluaran, cek saldo)
"""

from utils import bersihkan_layar, tampil_header, tampil_pesan, input_dengan_prompt, pause, validasi_angka
from prettytable import PrettyTable

def buat_catatan_baru(current_user, data_keuangan):
    """
    Membuat catatan keuangan baru untuk user
    Return: 'continue' atau 'logout'
    """
    bersihkan_layar()
    tampil_header("CATATAN BARU")
    
    tampil_pesan("Belum ada catatan keuangan.", "INFO")
    print()
    
    # Menu pilihan
    table = PrettyTable()
    table.field_names = ["NO", "PILIHAN"]
    table.add_row(["1", "Buat catatan baru"])
    table.add_row(["2", "Logout"])
    table.align["NO"] = "c"
    table.align["PILIHAN"] = "l"
    print(table)
    print()
    
    pilihan = input_dengan_prompt("Pilih menu (1-2): ")
    
    if pilihan == "1":
        while True:
            print()
            saldo_awal = input_dengan_prompt("Masukkan nominal awal tabungan: Rp ")
            
            valid, angka = validasi_angka(saldo_awal)
            
            if not valid:
                tampil_pesan("Input harus berupa angka positif!", "ERROR")
                continue
            
            data_keuangan[current_user] = {
                'saldo': angka,
                'riwayat': [f"Saldo Awal: Rp {angka:,}"]
            }
            
            tampil_pesan("Catatan berhasil dibuat!", "SUKSES")
            pause()
            return "continue"
    
    elif pilihan == "2":
        tampil_pesan("Logout...", "INFO")
        return "logout"
    else:
        tampil_pesan("Pilihan tidak valid!", "ERROR")
        pause()
        return "continue"

def cek_saldo(current_user, data_keuangan):
    """Menampilkan saldo dan riwayat transaksi"""
    bersihkan_layar()
    tampil_header("CEK SISA TABUNGAN")
    
    try:
        saldo = data_keuangan[current_user]['saldo']
        
        # Tampilkan saldo
        table_saldo = PrettyTable()
        table_saldo.field_names = ["INFORMASI", "NILAI"]
        table_saldo.add_row(["Saldo Saat Ini", f"Rp {saldo:,}"])
        table_saldo.align["INFORMASI"] = "l"
        table_saldo.align["NILAI"] = "r"
        print(table_saldo)
        print()
        
        # Tampilkan riwayat transaksi
        print("RIWAYAT TRANSAKSI (5 Terakhir):")
        table_riwayat = PrettyTable()
        table_riwayat.field_names = ["NO", "TRANSAKSI"]
        table_riwayat.align["NO"] = "c"
        table_riwayat.align["TRANSAKSI"] = "l"
        
        riwayat = data_keuangan[current_user]['riwayat']
        jumlah = len(riwayat)
        mulai = max(0, jumlah - 5)
        
        for i in range(mulai, jumlah):
            table_riwayat.add_row([i + 1 - mulai, riwayat[i]])
        
        print(table_riwayat)
        pause()
        
    except Exception as e:
        tampil_pesan(f"Terjadi kesalahan: {e}", "ERROR")
        pause()

def catat_pemasukan(current_user, data_keuangan):
    """Mencatat pemasukan"""
    bersihkan_layar()
    tampil_header("CATAT PEMASUKAN")
    print()
    
    while True:
        nominal = input_dengan_prompt("Masukkan nominal pemasukan: Rp ")
        
        valid, angka = validasi_angka(nominal)
        
        if not valid:
            tampil_pesan("Input harus berupa angka positif!", "ERROR")
            print()
            continue
        
        keterangan = input_dengan_prompt("Keterangan (opsional): ")
        
        if keterangan == "":
            keterangan = "Pemasukan"
        
        # Update data
        data_keuangan[current_user]['saldo'] += angka
        data_keuangan[current_user]['riwayat'].append(
            f"+ Pemasukan: Rp {angka:,} ({keterangan})"
        )
        
        # Tampilkan hasil
        table = PrettyTable()
        table.field_names = ["INFORMASI", "NILAI"]
        table.add_row(["Pemasukan", f"Rp {angka:,}"])
        table.add_row(["Keterangan", keterangan])
        table.add_row(["Saldo Baru", f"Rp {data_keuangan[current_user]['saldo']:,}"])
        table.align["INFORMASI"] = "l"
        table.align["NILAI"] = "r"
        print()
        print(table)
        
        tampil_pesan("Pemasukan berhasil dicatat!", "SUKSES")
        pause()
        break

def catat_pengeluaran(current_user, data_keuangan):
    """Mencatat pengeluaran"""
    bersihkan_layar()
    tampil_header("CATAT PENGELUARAN")
    
    try:
        saldo_sekarang = data_keuangan[current_user]['saldo']
        
        # Tampilkan saldo saat ini
        table_saldo = PrettyTable()
        table_saldo.field_names = ["INFORMASI", "NILAI"]
        table_saldo.add_row(["Saldo Saat Ini", f"Rp {saldo_sekarang:,}"])
        table_saldo.align["INFORMASI"] = "l"
        table_saldo.align["NILAI"] = "r"
        print(table_saldo)
        print()
        
        while True:
            nominal = input_dengan_prompt("Masukkan nominal pengeluaran: Rp ")
            
            valid, angka = validasi_angka(nominal)
            
            if not valid:
                tampil_pesan("Input harus berupa angka positif!", "ERROR")
                print()
                continue
            
            if angka > saldo_sekarang:
                tampil_pesan("PERINGATAN: Pengeluaran melebihi saldo!", "WARNING")
                konfirmasi = input_dengan_prompt("Lanjutkan? (y/n): ")
                if konfirmasi.lower() != "y":
                    tampil_pesan("Pengeluaran dibatalkan.", "INFO")
                    pause()
                    return
            
            keterangan = input_dengan_prompt("Keterangan (opsional): ")
            
            if keterangan == "":
                keterangan = "Pengeluaran"
            
            # Update data
            data_keuangan[current_user]['saldo'] -= angka
            data_keuangan[current_user]['riwayat'].append(
                f"- Pengeluaran: Rp {angka:,} ({keterangan})"
            )
            
            # Tampilkan hasil
            table = PrettyTable()
            table.field_names = ["INFORMASI", "NILAI"]
            table.add_row(["Pengeluaran", f"Rp {angka:,}"])
            table.add_row(["Keterangan", keterangan])
            table.add_row(["Saldo Baru", f"Rp {data_keuangan[current_user]['saldo']:,}"])
            table.align["INFORMASI"] = "l"
            table.align["NILAI"] = "r"
            print()
            print(table)
            
            tampil_pesan("Pengeluaran berhasil dicatat!", "SUKSES")
            pause()
            break
            
    except Exception as e:
        tampil_pesan(f"Terjadi kesalahan: {e}", "ERROR")
        pause()

def hapus_data(current_user, data_keuangan):
    """
    Menghapus data tabungan
    Return: True jika berhasil dihapus, False jika dibatalkan
    """
    bersihkan_layar()
    tampil_header("HAPUS DATA TABUNGAN")
    
    tampil_pesan("PERINGATAN: Data yang dihapus tidak dapat dikembalikan!", "WARNING")
    print()
    
    try:
        # Tampilkan informasi data
        table_info = PrettyTable()
        table_info.field_names = ["INFORMASI", "NILAI"]
        table_info.add_row(["Saldo Saat Ini", f"Rp {data_keuangan[current_user]['saldo']:,}"])
        table_info.add_row(["Total Transaksi", f"{len(data_keuangan[current_user]['riwayat'])} transaksi"])
        table_info.align["INFORMASI"] = "l"
        table_info.align["NILAI"] = "r"
        print(table_info)
        print()
        
        # Menu konfirmasi
        table_menu = PrettyTable()
        table_menu.field_names = ["NO", "PILIHAN"]
        table_menu.add_row(["0", "Ya, Hapus Data"])
        table_menu.add_row(["1", "Tidak, Batalkan"])
        table_menu.align["NO"] = "c"
        table_menu.align["PILIHAN"] = "l"
        print(table_menu)
        print()
        
        pilihan = input_dengan_prompt("Pilih menu (0-1): ")
        
        if pilihan == "0":
            data_keuangan[current_user] = {}
            tampil_pesan("Data tabungan berhasil dihapus!", "SUKSES")
            pause()
            return True
        elif pilihan == "1":
            tampil_pesan("Penghapusan dibatalkan.", "INFO")
            pause()
            return False
        else:
            tampil_pesan("Pilihan tidak valid!", "ERROR")
            pause()
            return False
            
    except Exception as e:
        tampil_pesan(f"Terjadi kesalahan: {e}", "ERROR")
        pause()
        return False
