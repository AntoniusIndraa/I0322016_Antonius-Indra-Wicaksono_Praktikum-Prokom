print('''
No    TIPE RUMAH   Harga
1    T45/84       550 Juta
2    T55/112      850 Juta
3    T60/120      950 Juta ''')
print('~'*50)
#input
tipe = int(input('Masukkan nomer dari tipe rumah yang diinginkan = '))
dp = float(input('Masukkan uang muka yang ingin dibayarkan = '))
waktu = float(input('Masukkan Jangka waktu dalam tahun = '))
harga1 = 550000000
harga2 = 850000000
harga3 = 950000000
bunga = .05
notaris = 2000000
provisi = 1500000
PNBP = 650000
baliknama = 1500000

print('~'*50)

#prosess
if tipe == 1 :
    if waktu == 0 :
        hutang = harga1-dp
        bayar = hutang
        harga = harga1
    else : 
        hutang = harga1-dp
        cicilan_bunga= ((bunga*hutang)*waktu)//(waktu*12)
        bayar = hutang//(12*waktu) + cicilan_bunga
        harga = harga1
        print(f'Besar Hutang = {hutang}')
        print(f'Cicilan pokok bulanan {hutang//(12*waktu)}')
        print(f'Cicilan bunga bulan pertama adalah Rp {cicilan_bunga} ')
        print(f'Total cicilan setiap bulanan = {bayar}')
elif tipe == 2 :
    if waktu == 0 :
        hutang = harga2-dp
        bayar = hutang
        harga = harga2
    else :
        hutang = harga2-dp
        harga = harga2
        cicilan_bunga = ((bunga*hutang)*waktu)//(waktu*12)
        bayar = hutang//(12*waktu) + cicilan_bunga
        print(f'Besar Hutang = {hutang}')
        print(f'Cicilan pokok bulanan {hutang//(12*waktu)}')
        print(f'Cicilan bunga bulan pertama adalah Rp {cicilan_bunga} ')
        print(f'Total cicilan setiap bulanan = {bayar}')
elif tipe == 3 :
    if waktu == 0 :
        hutang = harga3-dp
        bayar = hutang
        harga = harga3
    else :
        hutang = harga3-dp
        harga = harga3
        cicilan_bunga = ((bunga*hutang)*waktu)//(waktu*12)
        bayar = hutang//(12*waktu) + cicilan_bunga
        print(f'Besar Hutang = {hutang}')
        print(f'Cicilan pokok bulanan {hutang//(12*waktu)}')
        print(f'Cicilan bunga bulan pertama adalah Rp {cicilan_bunga} ')
        print(f'Total cicilan setiap bulanan = {bayar}')
else:
    dp = 0
    bayar = 0
    harga = 0
    notaris = 0
    provisi = 0
    PNBP = 0
    baliknama = 0
    print('Tipe rumah tidak ada')


#cicilan = ((bunga*hutang)*waktu)/(waktu*12)


#output
print('~'*50)
print(f'Uang muka                 = Rp {dp}')
print(f'Cicilan bulan pertama     = Rp {bayar}')
print(f'Biaya Notaris             = Rp {notaris} ')
print(f'Biaya Provisi             = Rp {provisi} ')
print(f'Pajak Pembelian           = Rp {.025*harga}')
print(f'PNBP                      = Rp {PNBP}')
print(f'Biaya Balik Nama          = Rp {baliknama}')
print(f'Total Pembayaran pertama  = Rp {dp + bayar + notaris + provisi + (.025*harga) + PNBP + baliknama}')