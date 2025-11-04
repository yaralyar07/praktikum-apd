from utils import bersihkan_layar
from autentikasi import login
from menu import menu_utama
from transaksi import buat_catatan_baru

users_data = {}
data_keuangan = {}

def main():
    print("Memulai Program Pencatat Keuangan...")
    print("Loading...")
    
    while True:
        current_user = login(users_data, data_keuangan)
        
        if current_user is None:
            break
        
        while True:
            if current_user not in data_keuangan or data_keuangan[current_user] == {}:
                result = buat_catatan_baru(current_user, data_keuangan)
                if result == "logout":
                    break
            else:
                menu_utama(current_user, data_keuangan)
                break
    
    print("\nProgram selesai. Terima kasih!")

if __name__ == "__main__":
    main()
