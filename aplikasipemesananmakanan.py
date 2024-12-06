import datetime

# Data awal
menu = [
    {"id": 1, "nama": "Nasi Goreng", "harga": 20000, "stok": 10},
    {"id": 2, "nama": "Mie Goreng", "harga": 15000, "stok": 8},
    {"id": 3, "nama": "Ayam Bakar", "harga": 25000, "stok": 5},
]

keranjang = []
riwayat_pemesanan = []

# Menampilkan menu makanan
def tampilkan_menu():
    print("\n--- Menu Makanan ---")
    for item in menu:
        print(f"{item['id']}. {item['nama']} - Rp{item['harga']} (Stok: {item['stok']})")

# Untuk menambah menu
def tambah_menu():
    nama = input("Masukkan nama menu: ")
    harga = int(input("Masukkan harga: "))
    stok = int(input("Masukkan stok: "))
    menu.append({"id": len(menu) + 1, "nama": nama, "harga": harga, "stok": stok})
    print("Menu berhasil ditambahkan!")

# Untuk menghapus menu
def hapus_menu():
    tampilkan_menu()
    id_menu = int(input("Masukkan ID menu yang ingin dihapus: "))
    global menu
    menu = [item for item in menu if item["id"] != id_menu]
    print("Menu berhasil dihapus!")

# Untuk mengedit menu
def edit_menu():
    tampilkan_menu()
    id_menu = int(input("Masukkan ID menu yang ingin diedit: "))
    for item in menu:
        if item["id"] == id_menu:
            item["nama"] = input(f"Nama baru ({item['nama']}): ") or item["nama"]
            item["harga"] = int(input(f"Harga baru ({item['harga']}): ") or item["harga"])
            item["stok"] = int(input(f"Stok baru ({item['stok']}): ") or item["stok"])
            print("Menu berhasil diperbarui!")
            return
    print("Menu tidak ditemukan.")

# Menambah ke keranjang
def tambah_ke_keranjang():
    tampilkan_menu()
    id_menu = int(input("Masukkan ID menu: "))
    jumlah = int(input("Masukkan jumlah: "))
    for item in menu:
        if item["id"] == id_menu:
            if jumlah <= item["stok"]:
                keranjang.append({"id": item["id"], "nama": item["nama"], "jumlah": jumlah, "harga": item["harga"]})
                item["stok"] -= jumlah
                print("Berhasil ditambahkan ke keranjang!")
                return
            else:
                print("Stok tidak mencukupi.")
                return
    print("Menu tidak ditemukan.")

# Menampilkan keranjang belanja
def tampilkan_keranjang():
    print("\n--- Keranjang Belanja ---")
    if not keranjang:
        print("Keranjang kosong.")
    else:
        for item in keranjang:
            print(f"{item['nama']} - {item['jumlah']} x Rp{item['harga']}")

# Menghitung total harga dengan diskon
def hitung_total():
    total = sum(item["jumlah"] * item["harga"] for item in keranjang)
    diskon = 0
    if total > 100000:
        diskon = total * 0.1
    return total, diskon

#   sistem pembayaran
def pembayaran():
    tampilkan_keranjang()
    total, diskon = hitung_total()
    print(f"\nTotal: Rp{total}")
    print(f"Diskon: Rp{diskon}")
    print(f"Total yang dibayar: Rp{total - diskon}")
    bayar = int(input("Masukkan jumlah pembayaran: "))
    if bayar >= total - diskon:
        kembalian = bayar - (total - diskon)
        print(f"Pembayaran berhasil Kembalian: Rp{kembalian}")
        riwayat_pemesanan.append({"tanggal": datetime.datetime.now(), "pesanan": keranjang.copy(), "total": total, "diskon": diskon})
        keranjang.clear()
    else:
        print("Pembayaran gagal. Uang tidak cukup.")

#  riwayat pemesanan
def tampilkan_riwayat():
    print("\n--- Riwayat Pemesanan ---")
    if not riwayat_pemesanan:
        print("Belum ada pemesanan.")
    else:
        for riwayat in riwayat_pemesanan:
            print(f"\nTanggal: {riwayat['tanggal']}")
            for item in riwayat["pesanan"]:
                print(f"- {item['nama']} x {item['jumlah']} (Rp{item['harga']} per item)")
            print(f"Total: Rp{riwayat['total']} (Diskon: Rp{riwayat['diskon']})")

# Program utama
def main():
    while True:
        print("\n--- Aplikasi Pemesanan Makanan ---")
        print("1. Tampilkan Menu")
        print("2. Tambah Menu")
        print("3. Hapus Menu")
        print("4. Edit Menu")
        print("5. Tambah ke Keranjang")
        print("6. Tampilkan Keranjang")
        print("7. Pembayaran")
        print("8. Riwayat Pemesanan")
        print("9. Keluar")
        pilihan = input("Pilih menu (1-9): ")
        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            tambah_menu()
        elif pilihan == "3":
            hapus_menu()
        elif pilihan == "4":
            edit_menu()
        elif pilihan == "5":
            tambah_ke_keranjang()
        elif pilihan == "6":
            tampilkan_keranjang()
        elif pilihan == "7":
            pembayaran()
        elif pilihan == "8":
            tampilkan_riwayat()
        elif pilihan == "9":
            print("Terima kasih telah menggunakan aplikasi ini semoga harimu menyenangkan ;) !")
            break
        else:
            print("Pilihan tidak ada Coba lagi")

# Menjalankan program
main()




