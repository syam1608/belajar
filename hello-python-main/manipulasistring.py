#op manipulasi  string
#menyambung string (concatenate)
nama_awal = "irham"
nama_tengah = "moch"
nama_akhir = "syam"
nama_lengkap = nama_awal + nama_tengah + nama_akhir
print (nama_lengkap)
#menghitung panjang string
panjang = len(nama_lengkap)
print (panjang)
#op untuk string
#mengecek apakah ada komponen char string di string
a = "a"
status = a in nama_lengkap
print (a + " ada di " + nama_lengkap + " = " + str(status))
A = "A"
status = A in nama_lengkap
print (a + " ada di " + nama_lengkap + " = " + str(status))
a = "a"
status = a not in nama_lengkap
print (a + " ada di " + nama_lengkap + " = " + str(status))
#mengulah string
print ("wk"*12)
#indexing
print ("index ke-0 : " + nama_lengkap[0])
print ("index ke-6 : " + nama_lengkap[6])
print ("index ke-1 : " + nama_lengkap[-1])
print ("index ke-0:3 : " + nama_lengkap[0:3])
print ("index ke-0:7 : " + nama_lengkap[0:8])
print ("index ke-0:2,4,6,8,10 " + nama_lengkap[0:11:2])
#item paling kecil
print ("paling kecil : " + min(nama_lengkap))
#paling besar
print ("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print ("ascii code untuk spasi adalah " + str(ascii_code))
data = 117
print ("char untuk ascii 117 adalah " + chr(data))
#op dalam bentuk menthod
data = "Babang tamvan"
jumlah = data.count("a")
print ("jumlah a pada " + data + " = " + str(jumlah))