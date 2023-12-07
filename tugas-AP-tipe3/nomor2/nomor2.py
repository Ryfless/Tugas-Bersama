jumlah_kendaraan = int(input("Masukan Jumlah Kendaraan: "))
pkb = 3000000
njkb = (pkb/2)*100
indeks_pajak1 = 0.02
indeks_pajak2 = 0.005
indeks_pajak = 0
tarif_pajak = 0
koefisien = 1

for i in range(jumlah_kendaraan):
    indeks_pajak += i
    
if jumlah_kendaraan >= 2:
    tarif_pajak = indeks_pajak1 + (jumlah_kendaraan - koefisien )*indeks_pajak2
else:
    tarif_pajak = indeks_pajak1
    
tarif_pajak_kendaraan = njkb * koefisien * tarif_pajak

print(tarif_pajak_kendaraan)

