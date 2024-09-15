print("\nSelamat datang di program IMS\n")
nama = str (input("Siapa nama anda ?"))
umur = int (input("beerapa Umur anda"))
while umur < 0 or umur > 100:
    print("umur harus o dan 100")
    umur = int(input("berapa umur anda?")or 0)
hobi = str (input("Apa Hobi anda ?"))
tempat_tinggal = str (input("Dimana anda tinggal ?"))

print("\nMohon dipehatikan data di bawah ini!,Hubungi kami jika anda salah memasukan data\n")
print("Nama",nama)
print("Umur",umur,"Tahun")
print("Hobi",hobi)
print("Tempat tinggal",tempat_tinggal)

print("\nSelanjutnya Silahkan Jawab Pertanyaan di Bawah ini\n")

soal_1 = int(input("Berapa hasil dari 4 + 5 = "))
if soal_1== 9:
    print("Jawaban anda benar")
elif soal_1=="sembilan":
    print("Jawaban anda benar")    
else:
    print("Jawaban anda kurang tepat")
   
soal_2 = (input("Siapa pendiri NU ?"))
if soal_2=="Kh Hasyim Asyari":
    print("Jawaban anda benar")
else:
    print("Jawaban anda kurang tepat")
print("Terimakasih telah menjawab")


