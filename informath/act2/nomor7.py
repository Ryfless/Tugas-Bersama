def konstan(nilai):
    def g(x):
        return nilai
    return g

g_konstan = konstan(2)

hasil1 = g_konstan("a")
hasil2 = g_konstan("b")
hasil3 = g_konstan("c")

print(f"Nilai dari g(a) = {hasil1}\nNilai dari g(b) = {hasil2}\nNilai dari g(c) = {hasil3}")
if (hasil1 == 2) and (hasil2 == 2) and (hasil3 == 2):
    print("fungsi g(x) adalah konstan")
else:
    print("fungsi g(x) tidak konstan")