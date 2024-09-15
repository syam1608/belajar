#setiap hasil operasi komprasi adalah boolean
#>,<,>=,<=,==,!=,is, is not

a = 6
b = 8
#lebih besar dari
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 7
print(b,">",7,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
#kurangdari

hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = a < 3
print(a,"<",3,"=",hasil)
#lebih dari sama dengan

hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = a >= 3
print(a,">=",3,"=",hasil)

#kurang dari sama dengan

hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = a <= 3
print(a,"<=",3,"=",hasil)

#sama dengan

hasil = a == 3
print(a,"==",3,"=",hasil)
hasil = a == 3
print(a,"==",3,"=",hasil)
#!samandengan

hasil = a != 3
print(a,"!=",3,"=",hasil)
hasil = a != 3
print(a,"!=",3,"=",hasil)

#is sebagai kompertif objektif

x = 5 #ini adalah assigment membuat objel
y = 5
print("nilai x = ,",x,",id = ",hex(id(x)))
print("nilai y = ,",y,",id = ",hex(id(y)))