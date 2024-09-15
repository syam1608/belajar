#operasi yang dapat di lakukan dengan penyingkatan
#oprasi di tambah assigment
a = 5
print ("nilai =",a)

a += 1 # ini sama dgn a = a + 1
print ("nilai -= 1,nilai a menjadi",a)

a -= 2 # ini sama dgn a = a - 2
print ("nilai -= 2,nilai a menjadi",a)

a *= 5 # ini sama dgn a = a * 5
print ("nilai *= 5,nilai a menjadi",a)

a /= 2 # ini sama dgn a = a / 2
print ("nilai /= 2,nilai a menjadi",a)

b = 10
print ("nilai b =",b)
#modulus
b %= 3
print ("nilai b %= 3,nilai b menjadi",b)

b = 10 
print ("nilai b =",b)

b //= 3  # ini sama dgn a = a // 3
print ("nilai //= 3,nilai b menjadi",b)
#pangkat
a = 5
print ("nilai a =")
a **= 3
print ("nilai **= 5,nilai a menjadi",a)
#op bitwise
c = True
print ("nilai c =",c)
c |= False
print ("nilai c |= ,nilai c menjadi",c)
c = False
print ("nilai c =",c)
c |= False
print ("nilai c |= ,nilai c menjadi",c)
#and
c = True
print ("nilai c =",c)
c &= False
print ("nilai c &= ,nilai c menjadi",c)
c = True
print ("nilai c =",c)
c &= True
print ("nilai c &= ,nilai c menjadi",c)
#xor
c = True
print ("nilai c =",c)
c ^= False
print ("nilai c ^= ,nilai c menjadi",c)
c = False
print ("nilai c =",c)
c ^= False
print ("nilai c ^= ,nilai c menjadi",c)
#geser2
d =0b0100
print ("nilai d =",format(d,"04b"))
d >>= 2
print ("nilai d >>= 2,nilai menjadi",format(d,"04b"))
d <<= 1
print ("nilai d <<= 1,nilai menjadi",format(d,"04b"))