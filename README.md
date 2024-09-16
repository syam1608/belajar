#latihan ditc 
import datetime
import os
mahasiswa_template = {
    'nama': 'nama',
    'nim':'00000000',
    'sks':'000',
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}
os.system("clear")
#os.system("cls")#untuk windows
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("~"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa["nama"]= input("Nama Mahasiswa: ")
mahasiswa["nim"]= input("Nim Mahasiswa: ")
mahasiswa["sks"]= input("SKS Mahasiswa: ")
TAHUN = int(input("Tahun Mahasiswa (yyyy): "))
BULAN = int(input("Bulan Mahasiswa (1-12): "))
HARI = int(input("Tanggal Mahasiswa (1-31): "))
mahasiswa['lahir']= datetime.datetime(TAHUN,BULAN,HARI)
print(mahasiswa)
