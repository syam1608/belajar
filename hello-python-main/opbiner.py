#biner atau masing2 bit
a = 9
b = 5
#bitwise or (/)
c = a | b
print ("\n========OR========")
print ("nilai:",a,",binary :",format(a,"08b"))
print ("nilai:",b,",binary :",format(b,"08b"))
print ("\n================(|)")
print ("nilai:",c,",binary :",format(c,"08b"))
#biner and
c = a & b
print ("\n========AND========")
print ("nilai:",a,",binary :",format(a,"08b"))
print ("nilai:",b,",binary :",format(b,"08b"))
print ("\n================(&)")
print ("nilai:",c,",binary :",format(c,"08b"))
c = a ^ b
print ("\n========XOR========")
print ("nilai:",a,",binary :",format(a,"08b"))
print ("nilai:",b,",binary :",format(b,"08b"))
print ("\n================(^)")
print ("nilai:",c,",binary :",format(c,"08b"))
c = ~a
print ("\n========NOT=========")
print ("nilai :",a,"binary :",format(a,"08b"))
print ("\n================(~)")
print ("nilai :",c,"binary :",format(c,"08b"))
print ("\n================(^)")
d = 0b00000001001
e = 0b11111111111
print ("nilai :",e^d,"binary :",format(e^d,"08b"))
#shifting
#shifting right (>>)
c = a >> 3
print ("\n=====================(shifright)")
print ("nilai :",a,"binary :",format(a,"08b"))
print ("\n======================(>>)")
print ("nilai :",c,"binary :",format(c,"08b"))
#shifting left (<<)
c = a << 2
print ("\n=====================(shifleft)")
print ("nilai :",a,"binary :",format(a,"08b"))
print ("\n======================(<<)")
print ("nilai :",c,"binary :",format(c,"08b"))
