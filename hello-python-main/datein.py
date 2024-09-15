#integer
data_integer = 7
print("data :",data_integer)
print("-bertipe :",type(data_integer))
#tipe data angka dgn koma(float)
data_float = 1,8
print("data :",data_float)
print("-bertipe :",type (data_float))
#data string kumpulan karakter
data_string = "ucup"
print("data :",data_string)
print("bertipe :",type(data_string))
#tipe data bollea true false
data_boolea = False
print("data :",data_boolea)
print("bertipe :",type(data_boolea))
# tipe data khusus bilangan kompleks
data_complex = complex(4,4)
print("data:",data_complex)
print("bertipe:",type(data_complex))
#tipe dari bahasa c
from ctypes import c_double
data_c_double = c_double=(21,1)
print("data:",data_c_double)
print("bertipe:",type (data_c_double))
#merubah ke satu data ke data lain (casting)
data_integer = 6;
print("data = ",data_integer,",type=",type(data_integer))

data_float = float (data_integer)
data_string= str (data_integer)
data_boolea = bool (data_integer)
data_complex = complex (data_integer)
print("data = ",data_float,"type=",type(data_float))
print("data =",data_string,"type=",type(data_string))
print("data=",data_boolea,"type=",type(data_boolea))
print("data=",data_complex,"type=",type(data_complex))

#input data user
data = input ("masukan data=")
print("data=",data,",type=",type(data))
#jika ingin mengambil int

angka = float(input("masukan angka:"))
angka = int(input("masukan angka:"))

print("data=",angka,",type=",type(angka))
#boolean
biner = bool (int(input("masukan nilai boolean:")))
print("data=",biner,",type=",type(biner))

