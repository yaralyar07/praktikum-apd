import os

login_berhasil = False
percobaan = 0

while login_berhasil == False:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 50)
    print("               SELAMAT DATANG")
    print("=" * 50)
    print()
    
    username = input("Username: ")
    password = input("Password: ")
    
    if username == "alyar" and password == "2509106043":
        print()
        print("Login berhasil!")
        input("Tekan Enter untuk melanjutkan...")
        login_berhasil = True
    else:
        percobaan = percobaan + 1
        print()
        print("ERROR! Username atau password salah.")
        
        if percobaan >= 3:
            print("Anda terlalu banyak melakukan upaya login. Program ditutup.")
            input("Tekan Enter untuk keluar...")
            exit()
        else:
            input("Tekan Enter untuk mencoba lagi...")

data_catatan = {}

while True:
    if data_catatan == {}:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 50)
        print("     CATATAN BARU")
        print("=" * 50)
        print()
        print("Belum ada catatan keuangan.")
        print()
        print("Apakah Anda ingin membuat catatan baru?")
        print("0. Ya")
        print("1. Tidak (Tutup Program)")
        print()
        
        pilihan_buat = input("Ketik angka untuk memilih: ")
        
        if pilihan_buat == "0":
            saldo_valid = False
            while saldo_valid == False:
                print()
                saldo_awal = input("Masukkan nominal awal tabungan: Rp ")
                
                if saldo_awal == "":
                    print("ERROR, Input tidak boleh kosong.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                cek_angka = True
                for angka in saldo_awal:
                    if angka not in "0123456789":
                        cek_angka = False
                        break
                
                if cek_angka == False:
                    print("ERROR, Input harus berupa angka.")
                    input("Tekan Enter untuk melanjutkan...")
                    continue
                
                saldo_awal = int(saldo_awal)
                saldo_valid = True
            
            data_catatan['saldo'] = saldo_awal
            data_catatan['riwayat'] = []
            data_catatan['riwayat'].append(f"Saldo Awal: Rp {saldo_awal}")
            
            print()
            print("Catatan berhasil dibuat!")
            input("Tekan Enter untuk melanjutkan...")
            
        elif pilihan_buat == "1":
            print()
            print("Program ditutup.")
            exit()
        else:
            print()
            print("ERROR! Pilihan tidak valid! Masukkan angka 0 atau 1.")
            input("Tekan Enter untuk melanjutkan...")
    
    else:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 50)
            print("     PROGRAM PENCATAT KEUANGAN")
            print("=" * 50)
            print()
            print("MENU UTAMA:")
            print()
            print("1. Cek Sisa Tabungan")
            print("2. Catat Pemasukan")
            print("3. Catat Pengeluaran")
            print("4. Hapus Data Tabungan")
            print("0. Keluar Program")
            print()
            
            pilihan_menu = input("Ketik angka untuk memilih: ")
            
            # 1
            if pilihan_menu == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=" * 50)
                print("     CEK SISA TABUNGAN")
                print("=" * 50)
                print()
                
                print(f"Saldo saat ini: Rp {data_catatan['saldo']}")
                print()
                print("Riwayat Transaksi:")
                print("-" * 50)
                
                jumlah_riwayat = len(data_catatan['riwayat'])
                mulai = 0
                if jumlah_riwayat > 5:
                    mulai = jumlah_riwayat - 5
                
                for i in range(mulai, jumlah_riwayat):
                    print(data_catatan['riwayat'][i])
                
                print()
                input("Tekan Enter untuk kembali...")
            
            # 2
            elif pilihan_menu == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=" * 50)
                print("     CATAT PEMASUKAN")
                print("=" * 50)
                print()
                
                input_valid = False
                while input_valid == False:
                    nominal = input("Masukkan nominal pemasukan: Rp ")
                    
                    if nominal == "":
                        print("ERROR! Input tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 50)
                        print("     CATAT PEMASUKAN")
                        print("=" * 50)
                        print()
                        continue
                    
                    cek_angka = True
                    for angka in nominal:
                        if angka not in "0123456789":
                            cek_angka = False
                            break
                    
                    if cek_angka == False:
                        print("ERROR! Input harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 50)
                        print("     CATAT PEMASUKAN")
                        print("=" * 50)
                        print()
                        continue
                    
                    nominal = int(nominal)
                    input_valid = True
                
                keterangan = input("Keterangan (opsional): ")
                
                if keterangan == "":
                    keterangan = "Pemasukan"
                
                data_catatan['saldo'] = data_catatan['saldo'] + nominal
                data_catatan['riwayat'].append(f"+ Pemasukan: Rp {nominal} ({keterangan})")
                
                print()
                print("Pemasukan berhasil dicatat!")
                print(f"Saldo baru: Rp {data_catatan['saldo']}")
                print()
                input("Tekan Enter untuk kembali...")
            
            # 3
            elif pilihan_menu == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=" * 50)
                print("     CATAT PENGELUARAN")
                print("=" * 50)
                print()
                
                saldo_sekarang = data_catatan['saldo']
                
                print(f"Saldo saat ini: Rp {saldo_sekarang}")
                print()
                
                input_valid = False
                batal = False
                
                while input_valid == False and batal == False:
                    nominal = input("Masukkan nominal pengeluaran: Rp ")
                    
                    if nominal == "":
                        print("ERROR! Input tidak boleh kosong!")
                        input("Tekan Enter untuk melanjutkan...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 50)
                        print("     CATAT PENGELUARAN")
                        print("=" * 50)
                        print()
                        print(f"Saldo saat ini: Rp {saldo_sekarang}")
                        print()
                        continue
                    
                    cek_angka = True
                    for angka in nominal:
                        if angka not in "0123456789":
                            cek_angka = False
                            break
                    
                    if cek_angka == False:
                        print("ERROR! Input harus berupa angka!")
                        input("Tekan Enter untuk melanjutkan...")
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("=" * 50)
                        print("     CATAT PENGELUARAN")
                        print("=" * 50)
                        print()
                        print(f"Saldo saat ini: Rp {saldo_sekarang}")
                        print()
                        continue
                    
                    nominal = int(nominal)
                    
                    if nominal > saldo_sekarang:
                        print()
                        print("PERINGATAN: Pengeluaran melebihi saldo!")
                        konfirmasi = input("Lanjutkan? (y/n): ")
                        if konfirmasi != "y":
                            print("Pengeluaran dibatalkan.")
                            input("Tekan Enter untuk kembali...")
                            batal = True
                    else:
                        input_valid = True
                
                if batal == False:
                    keterangan = input("Keterangan (opsional): ")
                    
                    if keterangan == "":
                        keterangan = "Pengeluaran"
                    
                    data_catatan['saldo'] = data_catatan['saldo'] - nominal
                    data_catatan['riwayat'].append(f"- Pengeluaran: Rp {nominal} ({keterangan})")
                    
                    print()
                    print("Pengeluaran berhasil dicatat!")
                    print(f"Saldo baru: Rp {data_catatan['saldo']}")
                    print()
                    input("Tekan Enter untuk kembali...")
            
            # 4
            elif pilihan_menu == "4":
                os.system('cls' if os.name == 'nt' else 'clear')
                print("=" * 50)
                print("     HAPUS DATA TABUNGAN")
                print("=" * 50)
                print()
                print("PERINGATAN: Data yang dihapus tidak dapat dikembalikan!")
                print()
                
                print(f"Saldo saat ini: Rp {data_catatan['saldo']}")
                print(f"Total transaksi: {len(data_catatan['riwayat'])} transaksi")
                print()
                print("Apakah Anda yakin ingin menghapus data ini?")
                print("0. Ya, Hapus")
                print("1. Tidak, Batalkan")
                print()
                
                pilihan_hapus = input("Ketik angka untuk memilih: ")
                
                if pilihan_hapus == "0":
                    data_catatan.clear()
                    
                    print()
                    print("Data tabungan berhasil dihapus!")
                    input("Tekan Enter untuk melanjutkan...")
                    break 
                elif pilihan_hapus == "1":
                    print()
                    print("Penghapusan dibatalkan.")
                    input("Tekan Enter untuk kembali...")
                else:
                    print()
                    print("ERROR! Pilihan tidak valid! Masukkan angka 0 atau 1.")
                    input("Tekan Enter untuk melanjutkan...")
            
            # 0
            elif pilihan_menu == "0":
                print()
                print("Terima kasih!")
                exit()
            
            else:
                print()
                print("ERROR! Pilihan tidak valid! Masukkan angka 0-4.")
                input("Tekan Enter untuk melanjutkan...")
