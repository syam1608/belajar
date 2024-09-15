#loooping dari lits 
#for loop
kumpulan_angka = [1,4,3,2,5,7,8]
for angka in kumpulan_angka:
    print(f"angka = {angka}")
peserta = ["damba","badak","cucurut"]
for nama in peserta:
    print(f"nama = {nama}")
# for lop and range
kumpulan_angka = [9,3,4,7,5,]
panjang = len(kumpulan_angka)
for i in range(panjang):
    print(f"angka ={kumpulan_angka}")
kumpulan_angka = [9,3,4,7,5,]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1
#lits comprehensioan
data = ["ronaldo",7,10,"messi"]


angka = [9,3,4,7,5,]
kuadrat = [i**2 for i in angka]
print(kuadrat) 
[print(f"data={i}") for i in data]
#Enumerate
data_lits = [7,"ronaldo",10,"messi",4,8]
for index,data in enumerate(data_lits):
    print(f"index={index},data,{data}")
