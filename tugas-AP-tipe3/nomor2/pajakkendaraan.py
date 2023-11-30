def hitung_njkb(pkb):
    return int((pkb / 2) * 100)

def hitung_tp(njkb, koefisien, tarif_pajak):
    return int(njkb * koefisien * tarif_pajak)

pkb = int(input("Masukkan pajak kendaraan anda yang ada di STNK: "))
sumbangan_wajib = int(input("Masukkan dana sumbangan wajib kecelakaan lalu lintas anda: "))
koefisien = int(input("Masukkan bobot koefisien kendaraan anda: "))
tarif_pajak_pertama = 0.2
tarif_pajak_kedua = 0.005

njkb = hitung_njkb(pkb)
tp_kedua = njkb * tarif_pajak_kedua
pajak_progresif = hitung_tp(njkb, koefisien, tarif_pajak_pertama + tp_kedua)

print("Pajak kendaraan = ", pkb)
print("Sumbangan Wajib Dana Kecelakaan Lalu Lintas Jalan anda adalah = ", sumbangan_wajib)
print("Tarif kedua kendaraan anda sebesar = ", tp_kedua)
print("Pajak progresif anda adalah = ", pajak_progresif)
