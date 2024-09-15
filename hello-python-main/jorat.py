print("## kalkulator sederhana ##")
print("=*===================================*")
print()

print("1.perjumlahan")
print("2.pengurangan")
print("3.perkalian")
print("4.pembagian")
print()

pilihan = int(input("input pilihan opras:"))
num1 = float(input('angka pertama:'))
num2 = float(input('angka kedua:'))
print()

if pilihan == 1:
  print('Hasil dari',num1,'+',num2,'=',round(num1+num2,2))
elif pilihan == 2:
  print('Hasil dari',num1,'-',num2,'=',round(num1-num2,2))
elif pilihan == 3:
  print('Hasil dari',num1,'*',num2,'=',round(num1*num2,2))
elif pilihan == 4:
  print('Hasil dari',num1,'%',num2,'=',round(num1%num2,2))
else:
  print('Maaf, pilihan menu belum tersedia')