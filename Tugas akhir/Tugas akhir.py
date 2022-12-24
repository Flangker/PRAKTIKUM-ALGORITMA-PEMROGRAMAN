pilihan="y"
while pilihan=="y":
    atasnama=input("Masukan Nama pembeli: ")
    tanggal=int(input("Isi Tanggal pembelian: "))
    bulan=int(input("Isi Bulan pembelian: "))
    tahun=int(input("Isi Tahun pembelian: "))
    print("""
    ==============================
    
    Exsa Mart
    Jln.kebanyakan jalan no 09
    (087633247)
    List Menu Warung 
 
    ==============================
    1. Telur : Rp 32.000
    2. Tepung : Rp 18.000
    3. Mie goreng : Rp 3.500
     4.Mie kuah : 4.000
    ==============================
    """)
    pesan=str(input("masukkan list nomor menu Warung ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    if pesan == "1":
        listnama= "Telur"
        harga=(32000*jumlahpesan)
        ppn= int(harga * 0.001)
        if jumlahpesan >= 5:
            diskon = int(harga*0.2)
            totalharga=int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga=int(harga+ppn)
    elif pesan == "2":
        listnama= "Tepung"
        harga = (18000*jumlahpesan)
        ppn = int(harga * 0.1)
        if jumlahpesan >= 5:
            diskon = int(harga * 0.001)
            totalharga =int(harga-diskon+ppn)
        else:
            diskon =(0)
            totalharga =int(harga+ppn)
    elif pesan == "3":
        listnama= "Mie goreng"
        harga=int(3500*jumlahpesan)
        ppn = int(harga * 0.001)
        diskon=0
        totalharga=int(harga+ppn)
    elif pesan == "4":
        listnama= "Mie Rebus"
        harga=int(4000*jumlahpesan)
        ppn = int(harga * 0.001)
        diskon=0
        totalharga = int(harga+ppn)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print("--------------------------")
    print("Atas Nama: ",atasnama)
    print("Waktu Pembelian: ",tanggal, bulan, tahun)
    print("--------------------------")
    print("Exsa Mart")
    print("Jln.kebanyakan jalan no 09")
    print("(087633247)")
    print("--------------------------")
    print("Menu :",listnama)
    print("Jumlah Pesan :", jumlahpesan)
    print("Harga :", harga)
    print("Diskon :", diskon)
    print("PPN :", ppn)
    print("--------------------------")
    print("Jumlah Bayar :", totalharga)
    print("--------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")