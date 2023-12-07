def hitung_njkb(pkb):
    return (pkb / 2) * 100

def hitung_tp(njkb, koefisien, tarif_pajak):
    return njkb * koefisien * tarif_pajak

pkb = int(input("Masukan pajak kendaraan anda yang ada di STNK: "))
sumbangan_wajib = int(input("Masukan dana sumbangan wajib kecelakaan lalu lintas anda: "))
koefisien = 1
tarif_pajak_pertama = 0.02
tarif_pajak_kedua = 0.005

njkb = hitung_njkb(pkb)
tp_kedua = tarif_pajak_pertama + tarif_pajak_kedua
pajak_progresif = hitung_tp(njkb, koefisien, tp_kedua)

print("Pajak kendaraan", pkb)
print("Sumbangan Wajib Dana Kecelakaan Lalu Lintas Jalan anda adalah = ", sumbangan_wajib)
print(f"Tarif kedua kendaraan anda sebesar = {tp_kedua * 100}%")
print("Pajak progresif anda adalah = {:,.0f}".format(pajak_progresif))