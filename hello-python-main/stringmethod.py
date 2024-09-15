#op dalam bentuk method

##merubah case dari string

#merubah semua ke upper case
salam = "broh!"
print ("normal = " + salam)
salam = salam.upper()
print ("upper = " + salam)
#merubah semua ke lower case
aneh = "Aku ApalaH"
print ("normal = " + aneh)
aneh = aneh.lower()
print ("lower = " + aneh)
#pengecekan is x method
salam = "Loba"
Apakah_lower = salam.islower()   #hasilnya bool
print (salam + " is lower = " + str(Apakah_lower)) 
Apakah_upper = salam.isupper()   #hasilnya bool
print (salam + " is upper = " + str(Apakah_upper))
#isalpha() untuk mengecek semua huruf
#isalnum() untuk huruf dan angka
#isdecimal() untuk angka saja
#isspace() untuk spasi,tab,new line
#istitle() semua kata dimulai huruf besar
judul = " Aku Adalah Spiderman"
cek_judul = judul.istitle() #boolean
print (judul + " is title = " + str(cek_judul))
#ngecek komponen startswith endswith
cek_starts = "Kunaon Euy".startswith("Kunaon")
print ("starts = " + str(cek_starts))
cek_end = "Kunaon Euy".endswith("Euy")
print ("end = " + str(cek_end))
#penggabungan komponen join() split()
pisah = ("Aku","Kamu","Dia")
gabungan = ",".join(pisah)
print (pisah)
print (gabungan)
gabungan = " ".join(pisah)
print (gabungan)
gabungan = ("AkuehmKamuehmDia")
print (gabungan.split("ehm"))
#alokasi karakter rjust ljust center
kanan = "kanan".rjust(10)
print ("'"+kanan+"'")
kiri = "kiri".ljust(10)
print ("'"+kiri+"'")
tengah = "tengah".center(10,"$")
print ("'"+tengah+"'")
#kebalikannya strip
tengah = "tengah".strip("$")
print ("'"+tengah+"'")