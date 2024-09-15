# not,or,and,xor
a = True
c = not a

print("data =",a)
print("data c =",c)
#Or
a = False
b = False
c = a or b
print(a,"Or",b,"=",c)
a = False
b = True
c = a or b
print(a,"Or",b,"=",c)
a = True
b = False
c = a or b
print(a,"Or",b,"=",c)
a = True
b = True
c = a or b
print(a,"Or",b,"=",c)
#and
a = False
b = False
c = a and b
print(a,"And",b,"=",c)
a = False
b = True
c = a and b
print(a,"And",b,"=",c)
a = True
b = False
c = a and b
print(a,"And",b,"=",c)
a = True
b = True
c = a and b
print(a,"And",b,"=",c)
#xor
a = False
b = False
c = a ^ b
print(a,"Xor",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"Xor",b,"=",c)
a = True
b = False
c = a ^ b
print(a,"Xor",b,"=",c)
a = True
b = True
c = a ^ b
print(a,"Xor",b,"=",c)