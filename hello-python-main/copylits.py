# a = ["Xin","Aang","Dudung"]
# print(a)
# b = a
# print(b)
# a [1]= "Misitar"
# print(a)
# c = a.copy()
# print ({hex(id(a))})
# print ({hex(id(b))})
# print ({hex(id(c))})
# c [1] = "Karol"
# print(a)
# print(b)
# print(c)
import copy
data_1 = [1,2]
data_2 = [6,2,3]
data_3 = [5,4]
lits_data = (data_1,data_2,data_3,7,8)
print(lits_data)

peserta0 = ["Faiz",4,"Laki-laki"]
peserta1 = ["Irham",19,"Laki-laki"]
peserta2 = ["Naila",15,"Wanita"]

lits_peserta = (peserta0,peserta1,peserta2)

print(lits_peserta)
for peserta in lits_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

lits_c = copy.deepcopy (lits_peserta)
print(f"peserta{lits_c}")
peserta0[0] = "Andik"
print(f"peserta{lits_c}")
print(f"peserta{lits_peserta}")

