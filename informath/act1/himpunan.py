def buat_himpunan(new):
    return set(new)

def tambah_elemen(himp, element):
    himp.add(element)

def hapus_elemen(himp, element):
    himp.discard(element)

def gabungan(himp1, himp2):
    return himp1.union(himp2)

def irisan(himp1, himp2):
    return himp1.intersection(himp2)

def selisih(himp1, himp2):
    return himp1.difference(himp2)

def main():
    himpunan1 = buat_himpunan([5, 0, 4, 2, 3, 8, 3, 1])
    himpunan2 = buat_himpunan([23, 12, 4, 10, 8, 31, 5])

    print("Himpunan A:", himpunan1)
    print("Himpunan B:", himpunan2)

    tambah_elemen(himpunan1, 0)
    hapus_elemen(himpunan2, "y")

    print("\nSetelah penambahan dan penghapusan elemen:")
    print("Himpunan A:", himpunan1)
    print("Himpunan B:", himpunan2)

    himpunan_gabungan = gabungan(himpunan1, himpunan2)
    himpunan_irisan = irisan(himpunan1, himpunan2)
    himpunan_selisih = selisih(himpunan1, himpunan2)

    print("\nHasil gabungan A dan B:", himpunan_gabungan)
    print("Hasil irisan A dan B:", himpunan_irisan)
    print("Hasil selisih A dan B:", himpunan_selisih)

main()