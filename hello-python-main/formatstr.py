#format str
##generic
nama = "irham"
format_str = f"hello {nama}"
print (format_str)
#angka
angka = 20005.5
format_str = f"angka {angka}"
print (format_str)
#boolean
boolean = False
format_str = f"boolean {boolean}"
print (format_str)
#bilangan bulat 
angka = 15
format_str = f"angka bilangan bulat = {angka:d}"
print (format_str)
#ribuan
angka = 2005
format_str = f"ribuan = {angka:,}"
print (format_str)
#jutaan
angka = 5000000123
format_str = f"jutaan = {angka:,}"
print (format_str)
#bilangan decimal
angka = 2006.54321
format_str = f"decimal = {angka:.3f}"
print (format_str)
#menampilkan leading zeero
angka = 2006.54321
format_str = f"decimal = {angka:012.3f}"
print (format_str)
#menampilkan plus minus dalam angka
angka_plus = 10
angka_minus = -10
format_plus = f"angka plus = {angka_plus:+d}"
format_minus = f"angka minus = {angka_minus:+d}"
print (format_plus)
print (format_minus)
#mengformat persen
angka = 0.045
format_str = f"persen = {angka:%}"
print (format_str)
#aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_str = f"harga Rp {harga*jumlah:,}"
print (format_str)
angka = 255
format_binary = f"binary {bin(angka)}"
format_octal = f"octar {oct(angka)}"
format_hex = f"hex {hex(angka)}"
print (format_binary)
print (format_octal)
print (format_hex)