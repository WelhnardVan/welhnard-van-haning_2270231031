# halaman 17 modul praktikum algoritma pemrograman
# create by Welhnard Van Haning 2270231031

#latihan konversi satuan temperature

#program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input('masukan suhu dalam celcius : '))
print("suhu adalah",celcius, "celcius")

#reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur, "reamur")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah" ,fahrenheit, "fahrenheit")

#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah" ,kelvin, "kelvin")