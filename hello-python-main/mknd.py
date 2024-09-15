# multi keys dan nesting dict
import datetime
mahasiswa1 = {
    "nama": 'irham',
    'nim':'11223344',
    'sks':'150',
    'beasiswa':True,
    'lahir':datetime.datetime(2005,8,16)
}
mahasiswa2 = {
    "nama": 'bujang',
    'nim':'22223344',
    'sks':'100',
    'beasiswa':True,
    'lahir':datetime.datetime(2002,7,10)
}
mahasiswa3 = {
    "nama": 'bojok',
    'nim':'33223344',
    'sks':'110',
    'beasiswa':False,
    'lahir':datetime.datetime(2006,2,16)
}
data_mahasiswa = {
    'MAH001':mahasiswa1,
    'Mah002':mahasiswa2,
    'MAH003':mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("~"*50)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks"]
    BEASISWA = data_mahasiswa[KEY]["beasiswa"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")

print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")




