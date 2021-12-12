#nama = input("Masukkan Nama anda:")

#def fungsisaya(nama):
#    print(f"Nama anda adalah {nama}")
#fungsisaya(nama)

# global x
# x = 20, semua x diluar function akan berubah 20.

#def fungsisaya(nama="", umur="", kelamin=""):
 #   print(f"nama anda {nama}, berumur {umur}, jenis kelamin {kelamin}")
#fungsisaya(nama = "rian", umur = 19, kelamin ="laki-laki")

#nama = input("nama anda : ")
#umur = int(input("umur anda adalah : "))
#kelamin = input("kelamin anda : ")
#fungsisaya(nama, umur, kelamin)

nama = []
def datanama(inputan):
    global banyak_data
    def simpandata(banyak_data):
        for i in range (banyak_data):
            nama_orang = input("Masukkan Nama : ")
            nama.append(nama_orang)
    def hapusdata():
        for posisi in range(len(nama)):
            print(posisi, nama[posisi])
        hapus = int(input("Input data yang ingin dihapus : "))
        nama.pop(hapus)
    if inputan == 1:
        banyak_data = int(input("banyak data yang di input :"))
        simpandata(banyak_data)
    elif inputan == 2:
        hapusdata()
    else:
        return
def tampilnama():
    for i in nama:
        print(i)
while True:
    print("#####################")
    print("#Menyimpan Data Nama#")
    print("######################")
    print("#1. Mengatur Data Nama#")
    print("#2. menampilkan Data Nama#")
    print("########################")
    

    pilihan = int(input(" Masukan Pilihan "))
    print()
    if pilihan == 1:
        print("pilihan: \n1. Simpan Data \n2. Hapus")
        inputan = int(input("Masukkan Data Nama: "))
        datanama(inputan)
        print()
    elif pilihan ==2:
       tampilnama()
       print()
    else:
        print("data tidak ada")
        print()

#datanama()
#tampilnama()

#def myfunction():
#    x=10
#    print("value inside function:", x)
#x=20
#myfunction ()
#print("value outside function", x)