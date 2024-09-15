#copy dan pop ditc
teman = {
   'r7':'ronaldo suuu',
   'pes':'messi angkara',
   'asp':'asep suratep',
   'ucp':'surucup'
   }
friend = teman.copy()

print(f"teman teman : {teman}\n")
print(f"friend : {friend}\n")
teman['pes']="messi sapuluh"
print(f"teman teman : {teman}\n")
print(f"friend : {friend}\n")
#pop ditc berdasarkan key
dataCup = friend.pop("ucp")
print(f"teman teman : {dataCup}\n")
print(f"friend : {friend}\n")
#data terakhir
dataterakhir = friend.popitem()
print(f"data terakhir : {dataterakhir}\n")
print(f"friend : {friend}\n")