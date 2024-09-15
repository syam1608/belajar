sisi = 10

#menggunakan for 1
count = 1
for i in range(sisi):
    print("$"*count)
    count += 1
#menggunakan while 1
count = 1
while True:
    print("$"*count)
    count += 1
    if count > sisi:
        break

#while 2
count = 1
while True:
    if (count%2):
        print("$"*count)
        count += 1
    else:
        count += 1
        break
#ganjil tok
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        print("$"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue
    if count > sisi:
        break
