#logika komperasi
#kurangdari
inputUser = float(input("\nMasukan angka kurang dari 5\natau\nLebih dari 12\n"))
isKurangDari = (inputUser < 5)
print ("Kurang dari 5 =",isKurangDari)
#lebih dari
isLebihDari = (inputUser > 12)
print ("Lebih dari 12 =",isLebihDari)
#correct
isCorrect = isKurangDari or isLebihDari
print("Angka anda masukan:",isCorrect)

#irisan
print("\n",12*"=","\n")
inputUser = float(input("\nMasukan angka Lebih dari 5\ndan\nKurang dari 12\n"))

isLebihDari = inputUser > 5
print ("Lebih dari 5 =",isLebihDari)

isKurangDari = inputUser < 12
print ("Kurang dari 12 =",isKurangDari)

isCorrect = isKurangDari or isLebihDari
print("Angka anda masukan:",isCorrect)
