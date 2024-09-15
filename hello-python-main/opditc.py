#operasi ditc
data_ditc = {
    "r7":"ronaldo suuu",
    "pes":"messi angkara",
    "bg":"bulan purnama"
}
print(data_ditc["r7"])
#panjang ditc
LENDITC = len(data_ditc)
print(f"panjang dict = {LENDITC}")
# mengecek key exist atau tidak
KEY = "r7"
CHECKEY = KEY in data_ditc
print(f"apakah {KEY}  ada di ditc {CHECKEY}")
#mengakses value (read) dengan git
print(data_ditc.get("r7"))
print(data_ditc.get("ha","tidak ada"))
#mengupdate dat
data_ditc ["r7"] = "ronaldo legend"
print(data_ditc)
data_ditc.update({"r7":"ronaldo suuu"})
print(data_ditc)
data_ditc.update({"ims":"irham keren"})
print(data_ditc)
#mendelete data ditc
del data_ditc["ims"]
print(data_ditc)