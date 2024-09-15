#index 0(-3) 1(-2) 2(-1)
data = ["Dadang","Naser","Uedien"]
#mengambil data 
data_0 = data[0]
print (data_0)
data_1 = data[-1]
print (data_1)
panjang_data = len(data)
print(panjang_data)
#menmbah data sesuai lits
data.insert (2,"Aang")
print(data)
#menambah di akhir 
data.append ("Xin")
print(data)
#data gabungan
new_data = ["Jin","Jan","Jun"]
data.extend(new_data)
print(data)
data[-1] = "Uejang"
print(data)
#remove
data.remove("Dadang")
print(data)
#remove akhir
data.pop()
print(data)