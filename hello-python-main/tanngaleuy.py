# date and time
import datetime as dt
hari_ini = dt.date.today()
print (hari_ini)
print (f"Hari ini adalah hari = {hari_ini:%A}")

hari_itu = dt.date(2005,8,16)
print (hari_itu)
print (f"Hari ini adalah hari = {hari_itu:%A}")

print ("Masukan tanggal lahir siapapun")
tanggal = int(input("Tanggal : "))
bulan = int(input("bulan : "))
tahun = int(input("tahun : "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print  (f"Tanggal lahir anda : {tanggal_lahir}")
print  (f"Harinya adalah :{tanggal_lahir:%A}")
hari_ini = dt.date.today()
print (f"Hari ini adalah hari = {hari_ini:%A}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
print (f"umur anda adalah : {umur_tahun} tahun")