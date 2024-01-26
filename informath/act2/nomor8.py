p = int(input("Masukan Angka: "))

kebenaran = False

if p == 1:
    print(f"{p} bukanlah angka prima")
elif p > 1:
    for i in range(2, p):
        if p % i == 0:
            kebenaran = True
            break
    if kebenaran:
        print(f"{p} adalah bukan bilangan prima!")
        print(f"{p} Tidak memenuhi syarat!")
    else:
        print(f"{p} adalah bilangan prima!")
        print(f"\nMaka negasi P adalah {kebenaran}")