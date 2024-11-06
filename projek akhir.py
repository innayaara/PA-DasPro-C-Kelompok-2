import json
import os
from prettytable import PrettyTable
import pwinput
import time

def clear():
    os.system("cls")

# Fungsi untuk menginisialisasi file yang diperlukan
def inisialisasi_file():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as file:
            json.dump([], file, indent=4)
            
# Fungsi untuk memuat data pengguna
def muat_pengguna():
    with open("users.json", "r") as file:
        return json.load(file)

# Fungsi untuk menyimpan data pengguna
def simpan_pengguna(pengguna):
    with open("users.json", "w") as file:
        json.dump(pengguna, file, indent=4)
        
# Fungsi untuk menyimpan data ke file JSON
def simpan_data(nama_file, data):
    with open(nama_file, 'w') as file:
        json.dump(data, file)

# Fungsi untuk memuat data produk
jsonPathProduk = r"produk.json"

# Membaca data produk dari file JSON
try:
    with open(jsonPathProduk, "r") as file:
        dataProduk = json.load(file)
except FileNotFoundError:
    print("File produk.json tidak ditemukan!")
    dataProduk = []
except json.JSONDecodeError:
    print("Terjadi kesalahan dalam membaca data produk.")
    dataProduk = []



# Fungsi untuk menyimpan dan memuat data
def simpan_produk(produk):
    with open('produk.json', 'w') as f:
        json.dump(produk, f, indent=4)

def simpan_pengguna(pengguna):
    with open('pengguna.json', 'w') as f:
        json.dump(pengguna, f, indent=4)

def muat_pengguna():
    try:
        with open('pengguna.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Fungsi untuk menampilkan produk
def tampilkan_produk():
    produk = dataProduk
    if not produk:
        print("Belum ada produk tersedia!")
        return
    
    tabel = PrettyTable()
    tabel.title = "Produk Perhiasan"
    tabel.field_names = ["Nama", "Harga", "Stok"]
    for detail in produk:
        Harga = int(detail["Harga"])
        tabel.add_row([
            detail["Nama"],
            f"Rp {Harga:,}",
            detail["Stok"]
        ])
    print(tabel)
    input("Tekan enter untuk melanjutkan...")

# Fungsi untuk menambah produk baru
def tambah_produk():
    produk = dataProduk
    
    nama = input("Masukkan nama produk: ")
    
    try:
        harga = int(input("Masukkan harga produk: Rp "))
        if harga <= 0:
            print("======================================")
            print("|      Harga harus lebih dari 0!     |")
            print("======================================")
            return
            
        stok = int(input("Masukkan stok produk: "))
        if stok < 0:
            print("======================================")
            print("|      Stok tidak boleh negatif!     |")
            print("======================================")
            return
            
    except ValueError:
        print("Harga dan stok harus berupa angka!")
        return
    except KeyboardInterrupt:
            print("jangan tekan ctrl")
            input("Tekan enter untuk melanjutkan.....")
    
    # Tambahkan produk baru ke list produk tanpa kode
    produk.append({
        "Nama": nama,
        "Harga": harga,
        "Stok": stok
    })
    
    simpan_produk(produk)
    print("======================================")
    print("|    Produk berhasil ditambahkan!    |")
    print("======================================")


# Fungsi untuk memperbarui produk
def perbarui_produk():
    produk = dataProduk
    
    if not produk:
        print("Belum ada produk tersedia!")
        return
        
    tampilkan_produk()
    nama_produk = input("Masukkan nama produk yang akan diperbarui: ")
    
    # Cari produk berdasarkan nama
    produk_ditemukan = None
    for item in produk:
        if item["Nama"].lower() == nama_produk.lower():
            produk_ditemukan = item
            break
    
    if not produk_ditemukan:
        print("======================================")
        print("|      Produk tidak ditemukan!       |")
        print("======================================")
        return
    
    print("\nBiarkan kosong jika tidak ingin mengubah")
    nama_baru = input(f"Masukkan nama baru ({produk_ditemukan['Nama']}): ")
    harga_baru = input(f"Masukkan harga baru (Rp {produk_ditemukan['Harga']:,}): ")
    stok_baru = input(f"Masukkan stok baru ({produk_ditemukan['Stok']}): ")
    
    # Memperbarui data produk
    if nama_baru:
        produk_ditemukan["Nama"] = nama_baru
    if harga_baru:
        try:
            harga_baru = int(harga_baru)
            if harga_baru <= 0:
                print("Harga harus lebih dari 0!")
                return
            produk_ditemukan["Harga"] = harga_baru
        except ValueError:
            print("Harga harus berupa angka!")
            return
        except KeyboardInterrupt:
            print("jangan tekan ctrl")
            input("Tekan enter untuk melanjutkan.....")
    if stok_baru:
        try:
            stok_baru = int(stok_baru)
            if stok_baru < 0:
                print("Stok tidak boleh negatif!")
                return
            produk_ditemukan["Stok"] = stok_baru
        except ValueError:
            print("Stok harus berupa angka!")
            return
        except KeyboardInterrupt:
            print("jangan tekan ctrl")
            input("Tekan enter untuk melanjutkan.....")
    
    simpan_produk(produk)
    print("======================================")
    print("|    Produk berhasil diperbarui!     |")
    print("======================================")

# Fungsi untuk menghapus produk
def hapus_produk():
    produk = dataProduk
    
    if not produk:
        print("Belum ada produk tersedia!")
        return
        
    tampilkan_produk()
    nama_produk = input("Masukkan nama produk yang akan dihapus: ")
    
    # Cari produk berdasarkan nama
    produk_ditemukan = None
    for item in produk:
        if item["Nama"].lower() == nama_produk.lower():
            produk_ditemukan = item
            break
    
    if not produk_ditemukan:
        print("======================================")
        print("|      Produk tidak ditemukan!       |")
        print("======================================")
        return
    
    # Konfirmasi penghapusan
    konfirmasi = input(f"Yakin ingin menghapus {produk_ditemukan['Nama']}? (y/n): ").lower()
    if konfirmasi == 'y':
        produk.remove(produk_ditemukan) 
        simpan_produk(produk)
        print("======================================")
        print("|     Produk berhasil dihapus!       |")
        print("======================================")
    else:
        print("======================================")
        print("|      Penghapusan dibatalkan         |")
        print("======================================")

# Fungsi untuk mencari produk
def cari_produk():
    produk = dataProduk
    
    if not produk:
        print("Belum ada produk tersedia!")
        return
        
    kata_kunci = input("Masukkan kata kunci pencarian: ").lower()
    
    # Mencari produk yang mengandung kata kunci pada nama
    hasil = [detail for detail in produk if kata_kunci in detail["Nama"].lower()]
    
    if hasil:
        tabel = PrettyTable()
        tabel.title = "Hasil Pencarian"
        tabel.field_names = ["Nama", "Harga", "Stok"]
        for detail in hasil:
            # Pastikan detail['Harga'] adalah angka
            try:
                harga = int(detail["Harga"])  # Mengonversi menjadi integer jika perlu
                tabel.add_row([
                    detail["Nama"],
                    f"Rp {harga:,}",
                    detail["Stok"]
                ])
            except ValueError:
                print(f"Data harga untuk {detail['Nama']} tidak valid.")
                continue  # Lanjutkan ke produk berikutnya
        print(tabel)
    else:
        print("======================================")
        print("|       Produk tidak ditemukan       |")
        print("======================================")

# Fungsi untuk mengurutkan produk
def urutkan_produk(user):
    produk = dataProduk  # Mengambil data produk
    
    if not produk:  # Cek apakah ada produk
        print("Belum ada produk tersedia!")
        return
        
    print("Urutkan berdasarkan:")  
    print("1. Nama")
    print("2. Harga")
    print("3. Stok")
    try:
        pilihan = input("Pilih opsi pengurutan (1-3): ")  
        if pilihan not in ["1", "2", "3"]:  
            print("Pilihan tidak valid!")
            return
            
        urutan = input("Urutan (1: Menaik, 2: Menurun): ")  
        if urutan not in ["1", "2"]:  
            print("Pilihan tidak valid!")
            return
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor.")
    except KeyboardInterrupt:
        print("jangan tekan ctrl C")
        try:
            input("Tekan enter untuk melanjutkan.....")    
        except KeyboardInterrupt:
            pass
    
    # Pemetaan pilihan ke key produk
    key_map = {"1": "Nama", "2": "Harga", "3": "Stok"}
    key = key_map[pilihan]
    reverse = urutan == "2"  
    
    # Mengurutkan produk berdasarkan kunci yang dipilih
    sorted_items = sorted(produk, key=lambda x: x[key], reverse=reverse)
    
    # Membuat tabel untuk menampilkan produk yang sudah diurutkan
    tabel = PrettyTable()
    tabel.title = f"Produk Diurutkan Berdasarkan {key}"
    tabel.field_names = ["Nama", "Harga", "Stok"]
    
    for detail in sorted_items:
        # Pastikan harga adalah integer untuk pemformatan
        harga = int(detail['Harga']) if isinstance(detail['Harga'], str) and detail['Harga'].isdigit() else detail['Harga']
        
        tabel.add_row([
            detail["Nama"],
            f"Rp {harga:,}",  
            detail["Stok"]
        ])
        
    print(tabel)  # Menampilkan tabel
    
def transaksi(user):
    produk = dataProduk  
    
    if not produk:
        print("Belum ada produk tersedia!")
        return
        
    tampilkan_produk()  
    nama_produk = input("Masukkan nama produk yang ingin dibeli: ").lower()
    
    # Mencari produk berdasarkan nama
    produk_ditemukan = None
    for detail in produk:  
        if detail["Nama"].lower() == nama_produk:
            produk_ditemukan = detail
            break
    
    if not produk_ditemukan:
        print("Produk tidak ditemukan!")
        return
    
    # Menggunakan satu blok try-except untuk memeriksa dan mengonversi data yang dibutuhkan
    try:
        jumlah = int(input("Masukkan jumlah yang ingin dibeli: "))
        if jumlah <= 0:
            print("Jumlah pembelian harus lebih dari 0!")
            return
        
        stok_produk = int(produk_ditemukan["Stok"])  
        harga_produk = int(produk_ditemukan["Harga"])  
        saldo_user = int(user["saldo"])  
    except ValueError:
        print("Data input tidak valid. Pastikan jumlah, stok, harga, dan saldo adalah angka yang valid.")
        return
    except KeyboardInterrupt:
        print("jangan tekan ctrl+c")
        try:
            input("Tekan enter untuk melanjutkan.....")    
        except KeyboardInterrupt:
            pass 

    if jumlah > stok_produk:
        print("Stok tidak mencukupi!")
        return

    total_harga = harga_produk * jumlah  
    
    if saldo_user < total_harga:
        print(f"Saldo tidak mencukupi! Total pembelian: Rp {total_harga:,}")
        return
    
    # Konfirmasi pembelian
    print(f"\nDetail Pembelian:")
    print(f"Produk: {produk_ditemukan['Nama']}")
    print(f"Jumlah: {jumlah}")
    print(f"Total: Rp {total_harga:,}")
    
    konfirmasi = input("Lanjutkan pembelian? (y/n): ").lower()
    if konfirmasi != 'y':
        print("Pembelian dibatalkan.")
        return
    
    # Proses pembelian
    produk_ditemukan["Stok"] = str(stok_produk - jumlah)  
    simpan_produk(produk)  
    
    # Update saldo pengguna
    pengguna = muat_pengguna()
    for p in pengguna:
        if p["username"] == user["username"]:
            p["saldo"] = str(saldo_user - total_harga)  
            user["saldo"] = p["saldo"]  
            break
    simpan_pengguna(pengguna)  
    
    # Menampilkan invoice
    print("\n=== INVOICE ===")
    print(f"Pembeli: {user['username']}")
    print(f"Produk: {produk_ditemukan['Nama']}")
    print(f"Jumlah: {jumlah}")
    print(f"Total: Rp {total_harga:,}")
    print(f"Sisa saldo: Rp {saldo_user - total_harga:,}")

# Fungsi untuk melihat saldo
def lihat_saldo(user):
    try:
        saldo_user = int(user['saldo'])  
        print(f"Saldo Anda: Rp {saldo_user:,}")
    except ValueError:
        print("Saldo tidak valid. Harap periksa data pengguna.")
    except KeyboardInterrupt:
            print("jangan tekan ctrl+C")
            input("Tekan enter untuk melanjutkan.....")

# Fungsi untuk top up saldo
def top_up_saldo(user):
    pilihan_nominal = [5000000, 7000000, 10000000, 15000000, 17000000, 20000000]
    
    # Menampilkan tabel pilihan nominal top-up
    tabel = PrettyTable()
    tabel.title = "Pilihan Nominal Top-Up"
    tabel.field_names = ["Nomor", "Nominal"]
    
    for i, nominal in enumerate(pilihan_nominal, 1):
        tabel.add_row([i, f"Rp {nominal:,}"])
    
    print("\n=== Pilihan Nominal Top-Up ===")
    print(tabel)
    
    try:
        pilihan = int(input("Pilih nominal top-up (1-4): "))
        if not (1 <= pilihan <= len(pilihan_nominal)):
            print("Pilihan tidak valid!")
            return
            
        jumlah = pilihan_nominal[pilihan - 1]
        
        # Update saldo di database
        pengguna = muat_pengguna()
        for p in pengguna:
            if p["username"] == user["username"]:
                try:
                    # Pastikan saldo yang dibaca adalah integer
                    saldo_terbaru = int(p["saldo"]) + jumlah  
                    p["saldo"] = saldo_terbaru  
                    user["saldo"] = saldo_terbaru  
                    break
                except:
                    print("Saldo tidak valid. Harap periksa data pengguna.")
        simpan_pengguna(pengguna)
        
        print(f"Top-up berhasil! Saldo Anda sekarang: Rp {user['saldo']:,}")
    except ValueError:
        print("Input tidak valid. Harap masukkan nomor.")
    except KeyboardInterrupt:
        print("jangan tekan ctrl C")
        try:
            input("Tekan enter untuk melanjutkan.....")    
        except KeyboardInterrupt:
            pass 
        
# Fungsi untuk registrasi
def registrasi():
    pengguna = muat_pengguna()
    username = input("Masukkan username: ")
    
    if any(user["username"] == username for user in pengguna):
        print("Username sudah digunakan!")
        return
    
    password = pwinput.pwinput("Masukkan password: ")
    
    pengguna.append({
        "username": username,
        "password": password,
        "role": "user",
        "saldo": 0
    })
    print("Selamat akun anda sudah di daftarkan.")
    simpan_pengguna(pengguna)

def menu_user(user):
    while True:
        clear()
        print("+====================================================================+")
        print("|                           Menu Pembeli                             |")
        print("+====================================================================+")
        print("| [1]. Lihat Produk                                                  |")
        print("| [2]. Transaksi Pembelian                                           |")
        print("| [3]. Lihat Saldo E-Money                                           |")
        print("| [4]. Top Up Saldo E-Money                                          |")
        print("| [5]. Cari Produk                                                   |")
        print("| [6]. Sorting Produk                                                |")
        print("| [7]. Logout                                                        |")
        print("+====================================================================+")
        try:                
            pilihan_pengguna = input("Pilihan opsi: ")
                            
            if pilihan_pengguna == "1":
                tampilkan_produk()
            elif pilihan_pengguna == "2":
                transaksi(user)
            elif pilihan_pengguna == "3":
                lihat_saldo(user)
            elif pilihan_pengguna == "4":
                top_up_saldo(user)
            elif pilihan_pengguna == "5":
                cari_produk()
            elif pilihan_pengguna == "6":
                urutkan_produk(user)
            elif pilihan_pengguna == "7":
                print("Logout berhasil.")
                break
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print("Masukkan huruf dan angka, bukan karakter simbol.")
        except KeyboardInterrupt:
            print("jangan tekan ctrl C")
            try:
                input("Tekan enter untuk melanjutkan.....")    
            except KeyboardInterrupt:
                pass
                break

def menu_admin():
    while True:
        print("+====================================================================+")
        print("|                             Menu Admin                             |")
        print("+====================================================================+")
        print("| [1]. Tampilkan Produk                                              |")
        print("| [2]. Tambah Produk                                                 |")
        print("| [3]. Perbarui Produk                                               |")
        print("| [4]. Hapus Produk                                                  |")
        print("| [5]. Cari Produk                                                   |")
        print("| [6]. Logout                                                        |")
        print("+====================================================================+")
        try:                
            pilihan_admin = input("Pilihan opsi: ")
                            
            if pilihan_admin == "1":
                tampilkan_produk()
            elif pilihan_admin == "2":
                tambah_produk()
            elif pilihan_admin == "3":
                perbarui_produk()
            elif pilihan_admin == "4":
                hapus_produk()
            elif pilihan_admin == "5":
                cari_produk()
            elif pilihan_admin == "6":
                print("Logout berhasil.")
                break
            else:
                print("Pilihan tidak valid")
        except ValueError:
            print("Masukkan huruf dan angka, bukan karakter simbol.")
        except KeyboardInterrupt:
            print("jangan tekan ctrl C")
            try:
                input("Tekan enter untuk melanjutkan.....")    
            except KeyboardInterrupt:
                pass  


def login(): 
    pengguna = muat_pengguna()
    try:
        username = input("Masukkan username: ")
        password = pwinput.pwinput("Masukkan password: ")

    # Cek untuk login sebagai admin
        if username == "admin" and password == "admin123":
            print("Login sebagai Admin berhasil!")
            menu_admin()
            return
    
    # Cek login untuk user biasa
        for user in pengguna:
            if user["username"] == username and user["password"] == password:
                print("Login berhasil!")
                menu_user(user)
                return

    # Jika loop selesai dan tidak ada kecocokan, beri opsi untuk mendaftar
        print("Mohon maaf, akun Anda tidak terdaftar.")
        pilih = input("Apakah Anda ingin mendaftar? (y/n): ").lower()
        if pilih == "y":
            registrasi()
        else:
            print("Silakan mendaftar terlebih dahulu untuk menggunakan sistem.")
    except ValueError:
        print("Masukkan huruf dan angka, bukan karakter simbol.")
    except KeyboardInterrupt:
            print("jangan tekan ctrl c")
            try:
                input("Tekan enter untuk melanjutkan.....")    
            except KeyboardInterrupt:
                pass    



def main():
    inisialisasi_file()
    while True:
        clear()
        print("\n === Menu Utama ===")
        print("1. Login")
        print("2. Registrasi")
        print("3. Keluar")
        try:
            pilihan = input("Pilih opsi: ")
        
            if pilihan == "1":
                login()
            elif pilihan == "2": 
                registrasi()
            elif pilihan == "3":
                print("Anda berhasil logout. Terima kasih telah menggunakan program ini!")
                break
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan huruf dan angka, bukan karakter simbol.")
        except KeyboardInterrupt:
            print("jangan tekan ctrl")
            try:
                input("Tekan enter untuk melanjutkan.....")    
            except KeyboardInterrupt:
                pass                    
main()