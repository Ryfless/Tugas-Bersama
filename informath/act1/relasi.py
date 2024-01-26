def kartesius(himpunan1, himpunan2):
    value = set()
    for e1 in himpunan1:
        for e2 in himpunan2:
            value.add((e1, e2))
    return value

def invers(relasi):
    vers = set()
    for i, j in relasi:
        vers.add((j, i))
    return vers

def compose(relasi, selasih):
    value = set()
    for a, i in relasi:
        for j, b in selasih:
            if i == j:
                value.add((a, b))
    return value


def main():
    himpunan1 = {3, 4, 5}
    himpunan2 = {"ani", "budi", "citra"}
    
    R = {(3, "ani"), (5, "budi"), (7, "citra")}
    S = {("citra", 5), ("dedi", 7), ("budi", 4)}

    print(f"<Relasi awal>\nRelasi 1: [{himpunan1}]\nRelasi2: [{himpunan2}]")

    print("\n<Product Kartesian>")
    print(f"himpunan1 x himpunan2 {kartesius(himpunan1, himpunan2)}")
    print(f"himpunan2 x himpunan1 {kartesius(himpunan2, himpunan1)}")

    print("\n<Fungsi Invers>")
    invers_R = invers(R)
    invers_S = invers(S)

    print(f"Relasi R: {R}")
    print(f"Relasi S: {S}")
    print(f"Invers R: {invers_R}")
    print(f"Invers S: {invers_S}")

    print("\n<Komposisi Relasi>")
    print(f"Hasil komposisi R dan S: {compose(R, S)}")
main()