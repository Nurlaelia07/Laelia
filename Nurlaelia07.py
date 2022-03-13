#type data
#boolean
2 > 3
3 < 6
#string
nama = ("Nurlaelia")
print(nama)
#integer
nilai = (2,3,5,6)
print(nilai)
#float
a = 12.4
print(a)
#mengecek tipe data
#string
nama = ("Nurlaelia")
print(nama,type(nama))
#float
a = 23.4
print(a)
nilai1 = int(input("masukkan nilai"))
nilai2 = int(input("masukkan nilai"))
#penjumlahan
print(nilai1+nilai2)
#perkalian
print(nilai1*nilai2)
#pengurangan
print(nilai1-nilai2)
#pembagian
print(nilai1/nilai2)
#sisa bagi
print(nilai1%nilai2)
#pangkat
print(nilai1**nilai2)
#pembagian bulat
print(nilai1//nilai2)

gaji_pokok = 1000000
gaji_lemburjam = 5000
lama_lembur = 21 #sesuai 2 angka terakhir nim
gaji_lembur = (gaji_lemburjam)*lama_lembur
pajak = 10/100
gaji_kotor = gaji_pokok + gaji_lembur
potongan = gaji_kotor * pajak
gaji_bersih = gaji_pokok - potongan
print("gaji_pokok = Rp. ", gaji_pokok)
print("gaji_lemburjam = Rp. ",gaji_lemburjam)
print("lama_lembur = Rp. ", lama_lembur)
print("gaji_lembur = Rp. ", gaji_lembur)
print("pajak = ", pajak)
print("gaji_kotor = Rp. ", gaji_kotor)
print("potongan = Rp. ", potongan)
print("gaji_bersih = Rp. ",gaji_bersih)

nilai_a = 7
nilai_b = 23
#tambah sama dengan +=
nilai_a += 4
nilai_b += 4
print(nilai_a)
print(nilai_b)
#-=
nilai_a -= 3
print(nilai_a)
# *=
nilai_b *= 5
print(nilai_b)
# /=
nilai_a /= 2
print(nilai_a)
# %=
nilai_b %= 6
print(nilai_b)
# **=
nilai_b **= 3
print(nilai_b)
# //=
nilai_a //= 4
print(nilai_a)

# ==
print(5 == 4)

# !=
print( 5 != 5)

# >
print( 2 > 3)

# <
print( 4 < 5)

# >=
print( 5 >= 4)

# <=
print( 7 <= 8)

# operator logika
# and
x = False
y = True
print(x and y)

# or
a = True
b = False
print(a or b)

# percabangan if 
nilai = 75
if (nilai >= 80):
    print ("Nilai A" )

#Percabangan if else 
nilai = 55
if (nilai >= 60):
       print ("LULUS")
else:
    print ("Tidak LULUS")
