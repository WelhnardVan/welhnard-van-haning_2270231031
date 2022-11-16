# Tugas Akhir praktikum algoritma pemrograman
# create by Welhnard Van Haning 2270231031

pilihan="y"
import datetime as dt
while pilihan=="y":
    print("""
    ==============================
             TEKNIK COFFEE
    ==============================
        List Menu Minuman Kopi 
    ==============================
    1. Kopi Susu    : Rp 5.000
    2. Kopi Coklat  : Rp 7.000
    3. Kopi Hitam   : Rp 4.000
    4. Kopi Luwak   : Rp 7.000
    ==============================
    """)
    pesan=str(input("masukkan list abjad menu kopi ="))
    jumlahpesan=int(input("masukkan jumlah pesanan ="))
    namapelanggan=str(input("masukan nama pelanggan ="))
    hari_ini = dt.date.today()

    if pesan == "1":
        listnama= "Kopi Susu"
        harga= (5000)
        totalharga=(5000*jumlahpesan)
    elif pesan == "2":
        listnama= "Kopi Coklat"
        harga = (7000)
        totalharga =(7000*jumlahpesan)
    elif pesan == "3":
        listnama= "Kopi Hitam"
        harga=int(4000)
        totalharga=int(4000*jumlahpesan)
    elif pesan == "4":
        listnama= "Kopi Luwak"
        harga=int(7000)
        totalharga = int(7000*jumlahpesan)
    else:
        listnama = "-"
        harga = "-"
        ppn = "-"
        diskon = "-"
        totalharga = "-"
        pilihan=input("menu tidak tersedia, silahkan masukkan abjad menu yang tersedia silahkan ulangi kembali Y/N =")
 
    print(                                   )
    print(                                   )
    print("---------------------------------")
    print("         TEKNIK COFFEE")
    print("Jl.Mari Sini Ngopi No.911 RT11/12")
    print("        NoHP:081234567891")
    print("---------------------------------")
    print("Nama            :", namapelanggan)
    print(f"{hari_ini}")
    print("---------------------------------")
    print("Menu            :", listnama)
    print("Jumlah Pesan    :", jumlahpesan)
    print("Harga           :", harga)
    print("---------------------------------")
    print("Jumlah Bayar    :", totalharga)
    print("---------------------------------")
    pilihan=input("apakah anda ingin order kembali Y/N =")