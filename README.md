# Praktikum Minpro 2
Maifariza Aulia Dyas | 2409116032 | Sistem Informasi A

Tema : Program To-Do-List Perusahaan 

# Flowchart
![Maifariza Aulia Dyas Minpro2 drawio (1)](https://github.com/user-attachments/assets/1ca403cc-00a5-4c88-8811-70d244f13617)

# Login
![Screenshot (90)](https://github.com/user-attachments/assets/5f66a81a-50df-427a-a2b4-695a58aa028a)


1. Pada menu Login user diminta untuk memasukkan Nama, NIM, dan Pin untuk mengetahui identitas user atau admin. Setelah itu login sebagai Perusahaan atau Karyawan.
2. Untuk role Perusahaan bisa melakukan CRUD (Create, Read, Update, dan Delete).
Sedangkan untuk role Karyawan hanya dapat menyelesaikan tugas dari Perusahaan.
* Jika user menginputkan angka selain 1 dan 2 maka tampilan akan kembali ke menu login.
  ![Screenshot (91)](https://github.com/user-attachments/assets/10bf6b52-8609-4998-826f-73ac5a311dbe)

  User bisa melakukan login kembali.
  
# Role Perusahaan 
![Screenshot (80)](https://github.com/user-attachments/assets/85ba982b-ab34-4cfb-a8ad-e8f319f32a8c)

Jika menginputkan angka 1 dan sebagai Perusahaan maka dengan otomatis akan menampilkan 5 role perusahaan dan admin diminta untuk menginputkan angka sesuai dengan role yang telah disediakan.


# Penjelasan Role Perusahaan
1. Tambah Tugas
   
![Screenshot (81)](https://github.com/user-attachments/assets/94ade6ff-8686-4e32-9191-4bcf2017bed3)

Input angka 1 untuk masuk ke role Tambah Tugas Perusahaan. Pada role Tambah Tugas ini menggunakan function def tambah_tugas() yang dimana function tersebut akan menampilkan sebuah tabel untuk kemudian admin dapat menambah data untuk dimasukkan ke dalam tabel.

![Screenshot (81)](https://github.com/user-attachments/assets/764dd48c-5d82-404c-8831-3292c1f2d29d)

Disini admin akan diminta memasukkan Nomor Tugas, Daftar Tugas, dan Deadline yang ingin ditambahkan. Dan admin akan ditanya apakah ingin Tambah Tugas kembali dengan pengulangan (ya/tidak).

* Admin memilih ya
  
![Screenshot (95)](https://github.com/user-attachments/assets/7b740f05-3767-47ae-ab0c-0cf65912d753)
Jika admin memilih "ya" otomatis kembali menginputkan "Nomor Tugas".

* Admin Memilih tidak
  
  ![Screenshot (94)](https://github.com/user-attachments/assets/5d51401d-c15d-46c6-bc73-d625476386eb)
  
  Sedangkan, jika admin memilih "tidak" maka tampilan akan kembali ke Role Perusahaan.

2. Lihat Tugas
   
   ![Screenshot (93)](https://github.com/user-attachments/assets/8ff0d6bf-9cb2-4fdb-af0e-06b5f29b2a88)
   Pada fitur ini user dapat melihat daftar tugas apa saja yang tersedia dengan print PrettyTabel.

4. Perbarui Tugas
   
  ![Screenshot (83)](https://github.com/user-attachments/assets/ca2a3486-213a-4f43-afed-0fae8d91616a)
  
Pada fitur ini admin bisa memperbarui tugas dengan memilih nomor semula dan memasukkan tugas serta deadline yang baru.

![Screenshot (84)](https://github.com/user-attachments/assets/6303ded8-a9f1-4e5d-bde0-f6ae7a08756d)

Input angka 2 untuk melihat tugas yang telah diperbarui.

4. Hapus Tugas
   ![Screenshot (85)](https://github.com/user-attachments/assets/08a3c983-c2c1-44f4-b004-1a8b4a7dc36d)
   Pada fitur ini admin menginputkan Nomor Tugas yang ingin dihapus.

   ![Screenshot (104)](https://github.com/user-attachments/assets/6570f620-5add-4232-a496-d84c45aef552)

   Input angka 2 untuk menampilkan perubahan data pada tabel.
* Sebelum di hapus
    ![Screenshot (85)](https://github.com/user-attachments/assets/49935bf6-1b53-4383-aab9-168bd4b26694)

* Setelah di hapus
![Screenshot (86)](https://github.com/user-attachments/assets/46a8ed5d-2124-46ca-8c0c-8a19004a5bd1)

5. Kembali Ke Menu Awal
   
   ![Screenshot (96)](https://github.com/user-attachments/assets/a5ad2f71-5be3-4d64-9874-939d40181714)

   Pada fitur ini admin akan diarahkan kembali ke menu login.

# Role Karyawan
![Screenshot (98)](https://github.com/user-attachments/assets/127b9a38-a7bb-467f-a1b3-c1236bf9dfdf)

Pada saat user menginputkan angka 2 maka user akan masuk ke Role Karyawan yang akan langsung menampilkan output dari daftar tugas perusahaan dengan menggunakan pretty table yang telah disediakan pada baris pemograman maupun pada role Tambah,Hapus,Lihat, Perbarui Tugas pada mode Perusahaan. Kemudian disini pembeli akan diminta untuk memasukan No. Tugas yang diinginkan.

![Screenshot (100)](https://github.com/user-attachments/assets/ac14a060-6136-42e6-9871-0d6a2984b5f2)

Jika user telah mengirim tugas akan ditanya kembali apakah ingin mengirim hal lain (ya/tidak)

* User memilih ya
  ![Screenshot (101)](https://github.com/user-attachments/assets/02ed49a5-8db6-414a-b708-5c30269be02a)

  Jika user memilih "ya", maka user kembali ke menu memasukkan tugas yang ingin dikirim kembali menggunakan looping atau pengulangan.

* User memilih tidak
![Screenshot (99)](https://github.com/user-attachments/assets/6c0b8505-2603-4c7e-ae53-480523124811)

Jika user memilih "tidak" maka otomatis tampilan seperti pada gambar diatas.
