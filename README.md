# Praktikum 6 - Sub Rutin / Fungsi
RIDHO FHADLY HAMZAH

312410486

TI.24.A5

# Penjelasan Kode
```python
data_mahasiswa = {}
```
Program dimulai dengan menginisialisasi dictionary untuk menyimpan Data Mahasiswa yang diinput.
```python
def tambah_data():
    print("\nMasukkan Data Mahasiswa")
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    data_mahasiswa[nama] = {
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }
    print("Data berhasil ditambahkan!")
```
Fungsi `def tambah_data` berfungsi untuk meminta pengguna menginputkan `Nama`, `NIM`, `Nilai Tugas`, `UTS` dan `UAS` serta mengakumulasikan semua nilai-nilai tersebut dan menyimpan hasil nya pada variabel `nilai_akhir`.
```python
def lihat_data():
    if not data_mahasiswa:
        print("=" * 64)
        print("No | Nama\t|    NIM    | Tugas | UTS | UAS |  Nilai Akhir |")
        print("=" * 64)
        print("   |                      Belum ada data                       |")
        print("=" * 64)
        return
    print("=" * 68)
    print("No | Nama\t|    NIM    | Tugas |  UTS  |  UAS  |  Nilai Akhir |")
    print("=" * 68)
    for i, (nama, data) in enumerate(data_mahasiswa.items(), start=1):
        print(f"{i:2} | {data['nama']}\t| {data['nim']} | {data['tugas']:.2f} | {data['uts']:.2f} | {data['uas']:.2f} | {data['nilai_akhir']:.2f}        |")
    print("=" * 68)
```
Fungsi `def lihat_data` berfungsi untuk menampilkan data mahasiswa yang sudah diinput sebelumnya, jika data masih kosong, maka program akan menampilkan pesan `Belum ada Data`.
```python
def hapus_data():
    nama = input("Masukkan Nama data yang ingin dihapus: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data atas nama {nama} berhasil dihapus!")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")
    lihat_data()
```
Fungsi `def hapus_data` berfungsi untuk menghapus data mahasiswa yang ingin dihapus dari dalam data melalui pencarian `Nama`.
```python
def ubah_data():
    nama = input("Masukkan Nama data yang ingin diubah: ")
    if nama in data_mahasiswa:
        print(f"Data ditemukan untuk nama {nama}. Masukkan data baru:")
        nim = data_mahasiswa[nama]['nim']
        nama_baru = input("Nama: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        nilai_akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
       
        data_mahasiswa[nama_baru] = {
            "nama": nama_baru,
            "nim": nim,
            "tugas": tugas,
            "uts": uts,
            "uas": uas,
            "nilai_akhir": nilai_akhir
        }
        if nama != nama_baru:
            del data_mahasiswa[nama]
        print(f"Data atas nama {nama} berhasil diubah!")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")
    lihat_data()
```
Fungsi `def ubah_data` berfungsi untuk mengubah/mengganti data mahasiswa yang ada di dalam daftar dengan data baru. 
```python
while True:
    print("="*46)
    print("|       Program Input Nilai Mahasiswa        |")
    print("="*46)
    print("|[(T) Tambah, (L) Lihat, (U) Ubah, (H) Hapus, (K) Keluar]|")
```
Selagi Program berjalan, maka program akan terus menampilkan `5` Menu.
```python
    pilihan = input("Masukkan Pilihan: ").lower()
    if pilihan == 't':
        tambah_data()
    elif pilihan == 'l':
        lihat_data()
    elif pilihan == 'h':
        hapus_data()
    elif pilihan == 'u':
        ubah_data()
    elif pilihan == 'k':
        print("Keluar dari Program")
        break
    else:
        print("Pilihan Tidak Valid.")
```
Jika pengguna memasukkan menu `'T'` maka program akan menampilkan fungsi `tambah_data` untuk menambah data.

Jika pengguna memasukkan menu `'L'` maka program akan menampilkan fungsi `lihat_data` untuk melihat daftar data.

Jika pengguna memasukkan menu `'U'` maka program akan menampilkan fungsi `ubah_data` untuk mengganti / mengubah data yang ada pada daftar.

Jika pengguna memasukkan menu `'H'` maka program akan menampilkan fungsi `hapus data` untuk menghapus data yang ada daftar.

Jika pengguna memasukkan menu `'K'` maka program akan berakhir dan menampilkan pesan `"Keluar dari program"`

# Flowchart
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Untitled%20Diagram(5)(1).drawio.png?raw=true)

# Hasil Kode
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-11-30%20073534.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-11-30%20073559.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-11-30%20073619.png?raw=true)
