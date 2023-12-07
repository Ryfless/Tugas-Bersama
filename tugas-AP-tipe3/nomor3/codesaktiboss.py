# Program Menghitung Gaji Karyawan

# Fungsi untuk menghitung gaji karyawan
def hitung_gaji(nama, golongan, jam_kerja):
    # Daftar gaji pokok dan tunjangan berdasarkan golongan
    gaji_pokok = [0, 1500000, 2000000, 2500000, 3000000]
    tunjangan = [0, 250000, 300000, 350000, 400000]

    # Jumlah jam kerja normal
    jam_normal = 173

    # Menghitung jam lembur
    if jam_kerja > jam_normal:
        jam_lembur = jam_kerja - jam_normal
    else:
        jam_lembur = 0

    # Menghitung gaji lembur
    gaji_lembur = jam_lembur * 20000

    # Menghitung total gaji pokok, gaji lembur, dan tunjangan
    total_gaji = gaji_pokok[golongan] + gaji_lembur + tunjangan[golongan]

    # Menghitung pajak gaji pokok dan lembur
    pajak_gaji_pokok = 0.05 * gaji_pokok[golongan]
    pajak_lembur = 0.05 * gaji_lembur

    # Menghitung total pajak
    total_pajak = pajak_gaji_pokok + pajak_lembur

    # Menghitung gaji bersih yang diterima karyawan
    gaji_diterima = total_gaji - total_pajak

    # Menampilkan hasil
    print("\nPROGRAM MENGHITUNG GAJI KARYAWAN")
    print("---------------------------------")
    print("MASUKAN NAMA\t\t:", nama)
    print("MASUKAN GOLONGAN\t:", golongan)
    print("MASUKAN JAM KERJA\t:", jam_kerja)
    print("\nNAMA\t\t\t:", nama)
    print("GAJI POKOK\t\t: RP {:,.2f}".format(gaji_pokok[golongan]))
    print("GAJI LEMBUR\t\t: RP {:,.2f}".format(gaji_lembur))
    print("PAJAK GAJI POKOK\t: RP {:,.2f}".format(pajak_gaji_pokok))
    print("PAJAK LEMBUR\t\t: RP {:,.2f}".format(pajak_lembur))
    print("TOTAL PAJAK\t\t: RP {:,.2f}".format(total_pajak))
    print("TUNJANGAN\t\t: RP {:,.2f}".format(tunjangan[golongan]))
    print("GAJI DITERIMA\t\t: RP {:,.2f}".format(gaji_diterima))

# Input data dari pengguna
nama = input("MASUKAN NAMA\t\t: ")
golongan = int(input("MASUKAN GOLONGAN\t: "))
jam_kerja = int(input("MASUKAN JAM KERJA\t: "))

# Panggil fungsi hitung_gaji
hitung_gaji(nama, golongan, jam_kerja)

