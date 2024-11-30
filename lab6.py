data_mahasiswa = {}

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

def hapus_data():
    nama = input("Masukkan Nama data yang ingin dihapus: ")
    if nama in data_mahasiswa:
        del data_mahasiswa[nama]
        print(f"Data atas nama {nama} berhasil dihapus!")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")
    lihat_data()

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

while True:
    print("="*46)
    print("|       Program Input Nilai Mahasiswa        |")
    print("="*46)
    print("|[(T) Tambah, (L) Lihat, (U) Ubah, (H) Hapus, (K) Keluar]|")

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