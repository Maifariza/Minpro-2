# Login Sederhana menggunakan Nama, NIM, Pin
nama = input("Masukan Nama Anda: ")

# Memasukan NIM 
while True:
    try:
        nim = int(input("Masukan NIM Anda: "))
        break 
    except ValueError:
        print('=========== NIM harus berupa angka! Silahkan coba lagi ===========')

# Memasukan PIN dan menggunakan angka
while True:
    try:
        pin = input('Masukkan PIN (harus 6 angka): ')
        if len(pin) != 6 or not pin.isdigit():
            raise ValueError
    except ValueError:
        print('=========== PIN harus terdiri dari 6 angka! Silahkan coba lagi ===========')
        continue
    print(f"Hola!, Selamat Datang {nama} dengan PIN {pin}") 
    break
print("\n") 

from prettytable import PrettyTable

# PrettyTable
table = PrettyTable()
table.field_names = ["Nomor Tugas", "Daftar Tugas", "Deadline"]

def tambah_tugas(nomor_tugas, daftar_tugas, deadline):
    table.add_row([nomor_tugas, daftar_tugas, deadline])

# Daftar Tugas Perusahaan
tambah_tugas("1", "Membuat Pembukuan Keuangan Kantor", "10-12-2024")
tambah_tugas("2", "Melakukan Posting Jurnal Operasional", "11-12-2024")
tambah_tugas("3", "Membuat Pembukuan dari Transaksi Keuangan Perusahaan", "14-12-2024")
tambah_tugas("4", "Membuat Laporan Keuangan", "14-12-2024")
tambah_tugas("5", "Melakukan pencatatan dan dokumentasi", "19-12-2024")
tambah_tugas("6", "Melakukan verifikasi kelengkapan Dokumen Perusahaan", "20-12-2024")

def home():
    while True:
        print(f"====== Login  ======")
        print(f"===== Company ======")
        print("1. Perusahaan")
        print("2. Karyawan")
        pilihan = input("Login Sebagai:")
        if pilihan == "1":
            perusahaan()
        elif pilihan == "2":
            karyawan()
            break
        else:
            print("Metode login tidak tersedia")

# Role Perusahaan
def perusahaan():
    while True:
        print("\n----- Atur To-Do-List Perusahaan 👩‍💻📋 -----")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Perbarui Tugas")
        print("4. Hapus Tugas")
        print("5. Kembali ke Menu Awal")
        pilihan = input("Pilih Role Perusahaan:")
        if pilihan == '1':
            tambah_tugas_input()
        elif pilihan == '2':
            lihat_tugas()
        elif pilihan == '3':
            perbarui_tugas()
        elif pilihan == '4':
            hapus_tugas()
        elif pilihan == '5':
            return
        else:
            print("Pilihan Tidak Tersedia")

def tambah_tugas_input():
    while True:
        print(table)
        nomor_tugas = input("Nomor Tugas:")
        daftar_tugas = input("Input Daftar Tugas Baru: ")
        deadline = input("Deadline:")
        tambah_tugas(nomor_tugas, daftar_tugas, deadline)
        print(f"No.[{nomor_tugas}] {daftar_tugas} dengan deadline {deadline}")
        daftar = input("Apakah ingin menambahkan tugas lagi? (ya/tidak):")
        if daftar == "tidak":
            break

def lihat_tugas():
    print(table)
    
def hapus_tugas():
    while True:
        lihat_tugas()
        nomor_tugas = input("Masukkan nomor tugas yang ingin dihapus.")

        for row in table._rows:
            if row[0] == nomor_tugas:
                table.del_row(table.rows.index(row))
        print(f"Nomor Tugas {nomor_tugas} telah berhasil dihapus: ")
        pilihan = input("Apakah Ingin menghapus barang lagi? (ya/tidak): ")
        if pilihan == "tidak":
            break
    
def perbarui_tugas():
    lihat_tugas()
    nomor_tugas = input("Masukkan Nomor Tugas Semula: ")
    revisi_tugas = input("Masukkan Tugas Baru: ")
    revisi_deadline = input("Masukkan Deadline Baru: ")
    for row in table._rows:
        if row[0] == nomor_tugas:
            row[1] = revisi_tugas
            row[2] = revisi_deadline
            print(f"Tugas dengan Nomor {nomor_tugas} berhasil diperbarui.")
            return
    print(f"Tugas dengan nomor {nomor_tugas} tidak ditemukan.")

    # Memperbarui tugas
    perbarui_tugas()

    # Melihat daftar tugas setelah diperbarui
    lihat_tugas()

# Karyawan
def karyawan():
    nama = str(input("Masukkan nama anda: "))
    print(f"===== Selamat Datang {nama} Di To-Do-List Company 🖥️📋! =====")
    while True:
        lihat_tugas()
        nomor_tugas = input("Masukkan Nomor Tugas Yang Akan Dipilih:")
        found = False
        for row in table._rows:
            if row[0] == nomor_tugas:
                found = True
                nama_tugas = input("Masukkan Tugas yang Ingin Dikirimkan: ")
                tanggal = input("Masukkan Tanggal Anda Mengirim Tugas: ")
                print(f"Tugas {nomor_tugas} {nama_tugas} Berhasil Terkirim Pada {tanggal}")

                # Menambah Tugas Karyawan Ke Table
                tambah_tugas(nomor_tugas, nama_tugas, tanggal)
                print(f"Tugas baru berhasil ditambahkan ke daftar.")

                kembali = input("Apakah ingin mengirim hal lain? (ya/tidak): ")
                if kembali == "tidak":
                    print("\n") 
                    print(f"===== Terimakasih Telah Menggunakan To-Do-List Company Kami =====")
                    return 
            
home()
