n = int(input("Masukan index: "))

for bar in range(2, n + 2):
    for kol in range(1, n + 3):
        if kol >= 2 and kol <= n+n and kol == bar:
            print("*", end = "")
        else:
            print(kol, end = "")
    print()
