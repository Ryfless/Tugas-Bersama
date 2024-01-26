def invers(relasi):
    himp = set()
    for a, b in relasi:
        himp.add((b, a))
    return himp

def main():
    himpunan1 = {2, 4, 8}
    himpunan2 = {"KB", "MB"}
    relasi_awal = {(2, "MB"), (4, "KB"), (8, "KB")}

    relasi_invers = invers(relasi_awal)

    print(f"Anggota himpunan1: {himpunan1}")
    print(f"Anggota himpunan2 = {himpunan2}")
    print(f"Relasi awal: {relasi_awal}")
    print(f"Relasi Invers: {relasi_invers}")
main()