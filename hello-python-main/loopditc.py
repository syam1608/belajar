#looping ditc
data = {
   'r7':'ronaldo suuu',
   'pes':'messi angkara',
   'asp':'asep suratep',
   'ucp':'surucup'
}
#looping firts try (yang keluar key nya)
for data1 in data:
    print(data1)
#mengambil items/ iterabels
key = data.keys()
print(key)
for key in data.keys():
    print(data.get(key))    
values = data.values()
for value in data.values():
    print(value)
items = data.items()
print(items)
for item in data.items():
    print(item)
for key,value in data.items():
    print(f"key = {key}, value = {value}")        