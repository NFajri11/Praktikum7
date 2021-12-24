print('\033[1m','\33[34')
print("=" * 65)
print("  |\tProgram Input Mahasiswa Menggunakan Fungsi\t|  ")
print("=" * 65)

dataMahasiswa = {}

class mahasiswa(object) :
    def tambah():
            nama = str(input("Mahasiswa Nama : "))
            nim = int(input("Masukan nim : "))
            tugas = int(input("Masukan nilai tugas : "))
            uts = int(input("Masukan nilai uts : "))
            uas = int(input("Masukan nilai uas : "))
            akhir = (tugas / 3) + (uts / 3.5) + (uas / 3.5)
            dataMahasiswa[nama] = nim, tugas ,uts , uas, akhir,
            print("\33[32m\nData Berhasil Di Tambahkan")
    def tampilkan() :
            print('\033[1m','\33[34m')
            print("=" * 100)
            print("|" + "\t" * 5 + "Daftar Nilai Mahasiswa" + "\t" * 5 +  "   |")
            print("|  \tnama\t  |  \tnim\t  |  \ttugas\t  |  \tuts\t  |  \tuas\t  |  \takhir      |")
            print("=" * 100)
            for tampil in dataMahasiswa.items():
                print("|  {0:14} |   {1: 6}    |    {2:5}      |       {3:3}    |     {4:3}      |     {5:5}       |"
                .format(tampil[0], tampil[1][0], tampil[1][1], tampil[1][2], tampil[1][3],"%.2f" % float(tampil[1][4])))
                print("=" * 100)
    def hapus (nama):
                del dataMahasiswa[nama]
                print("\33[31mData Berhasil Di Hapus ") 
    def ubah(nama):
            if nama in dataMahasiswa.keys():
                nim = int(input ("Masukan nim : "))
                tugas = int(input("Masukan tugas : "))
                uts = int(input("Masukan Nilai uts : "))
                uas = int(input("Masukan Nilai uas : "))
                akhir = (tugas / 3 ) + (uts / 3.5) + ( uas / 3.5 )
                dataMahasiswa[nama] =nim , tugas , uts , uas , akhir 
                print ("\33[33m\nData Berhasil Di Ubah ")
            else :
                print("\33[31m\Data Tidak Di Temukan")




while True :
    data = input ("\033[1m \33[34m \n 1 - Tambah Data\t 2 - Tampilkan Data\t 3 - Hapus Data\t 4 - Ubah Data\t5 - Keluar\t : "
    )
    if (data.lower() == '1'):
        mahasiswa.tambah()

    elif (data.lower() == '4'):
        nama = str(input("Masukan nama : "))
        mahasiswa.ubah(nama)
    elif (data.lower() == '3'):
        nama = str(input("Masukan nama :"))
        if nama in dataMahasiswa:
            mahasiswa.hapus(nama)
        else :
            print("\33[31mData Tidak Di Temukan ".format(nama))    
    elif (data.lower() == '2') :
        if dataMahasiswa.items():
            mahasiswa.tampilkan()
        else :
            print('\033[2m','\33[34m')
            print("=" * 69)
            print("| no |t\nama\t|\tnim\t|\ttugas\t|\tuts\t|\tuas\t|\takhir\t |")
            print("="  * 69)
            print("|   " + "\t" * 3 + "\33[31mTidak Ada Data" + "\t" * 4 + "  |")
            print("="  * 69)
    elif (data.lower() == '5') :
            print("\33[7m\nTkans You\n")
            print('\33[30m')
            exit() 
    else:
        print("\33[31mPilihan Tidak Tidak Tersedia ")
        