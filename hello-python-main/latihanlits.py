#latihan lits
lits_buku = []
while True:
    print("Masukan judul buku")
    judul = input("judul buku\t: ")
    penulis =input("penulis buku\t; ")
    
    buku_baru = [judul,penulis]
    lits_buku.append,(buku_baru)
    
    print("="*10,"Data buku","="*10)
    for index,buku in enumerate(lits_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    
    print("\n\n","="*20)
    isLanjut = input(f"Apakah mau lanjut?(y/n)")
    
    if isLanjut == "n":
        break