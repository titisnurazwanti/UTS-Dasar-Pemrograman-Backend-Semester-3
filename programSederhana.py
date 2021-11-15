# Kementrian Agama RI telah menetapkan dalam Peraturan Menteri Agama No 31 tahun 2019 bahwa;
# 1. Nisab zakat penghasilan / profesi senilai 85 gram emas
# 2. Kadar zakat pendapatan dan jasa 2,5%

print("======================================")
print("== PROGRAM MENGHITUNG ZAKAT PROFESI ==")
print("======================================")
print("Menurut Kaidah Zakat Profesi")
print("Menghitung Dengan Pengeluaran Bulanan")
print("======================================")
print(" ")

# Variabel list
namaMuzaki = []
gajiSebulanMuzaki = []
pengeluaranSebulanMuzaki = []
hargaEmas = []
gajiSetahunMuzaki = []
pengeluaranSetahunMuzaki = []
sisaGaji = []
nishab = []
zakat = []

banyakData = int(input("Berapa banyak data yang akan di masukkan? "))
print("======================================")
print(" ")

# looping inputan
for i in range(banyakData):
    nama = input("Masukkan nama : ")
    namaMuzaki.append(nama)
    emas = int(input("Masukkan harga emas saat ini /gram : "))
    hargaEmas.append(emas)
    gaji = int(input("Gaji perbulan : "))
    gajiSebulanMuzaki.append(gaji)
    pengeluaran = int(input("Pengeluaran perbulan : "))
    pengeluaranSebulanMuzaki.append(pengeluaran)
    print("======================================")
    print(" ")

# looping proses
for i in range(banyakData):
    a = 12 * gajiSebulanMuzaki[i]
    gajiSetahunMuzaki.append(a)
    b = 12 * pengeluaranSebulanMuzaki[i]
    pengeluaranSetahunMuzaki.append(b)
    c = gajiSetahunMuzaki[i] - pengeluaranSetahunMuzaki[i]
    sisaGaji.append(c)
    d = 85 * hargaEmas[i]
    nishab.append(d)
    e = 0.025 * sisaGaji[i]
    zakat.append(e)

# Looping hasil akhir
for i in range(banyakData):
    print("=============+++======+++=============")
    print("          Hasil  Perhitungan          ")
    print("=============+++======+++=============")
    print("Nama Muzaki          : ", namaMuzaki[i])
    print("======================================")
    print("Penghasilan Perbulan : ", gajiSebulanMuzaki[i])
    print("Penghasilan Pertahun :  " f'12 * {gajiSebulanMuzaki[i]} = {gajiSetahunMuzaki[i]}')
    print("Pengeluaran Perbulan : ", pengeluaranSebulanMuzaki[i])
    print("Pengeluaran Pertahun :  " f'12 * {pengeluaranSebulanMuzaki[i]} = {pengeluaranSetahunMuzaki[i]}')
    print("Sisa Penghasilan     :  " f'{gajiSetahunMuzaki[i]} - {pengeluaranSetahunMuzaki[i]} = {sisaGaji[i]}')
    print("Harga 1 Gram Emas    : ", hargaEmas[i])
    print("Nishab Yang Diperoleh: ", nishab[i])
    print("Perhitungan Zakat    :  " f'2,5% * {sisaGaji[i]} = {zakat[i]}')

    # Kondisi if
    if sisaGaji[i] >= nishab[i]:
        print("======================================")
        print("KETERANGAN : ANDA WAJIB ZAKAT")
        print("Sebanyak   : Rp.", zakat[i] , "/tahun")
        print("======================================")
        print(" ")

    if sisaGaji[i] < nishab[i]:
        print("======================================")
        print("KETERANGAN : ANDA TIDAK WAJIB ZAKAT")
        print("======================================")
        print(" ")