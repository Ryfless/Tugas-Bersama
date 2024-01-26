def konstan(nilai):
    def p(x):
        return nilai
    return p

n = 10**1000

p_konstan = konstan(n)

hasil1 = p_konstan("N")

print(f"Nilai dari p(n) = {hasil1}")
if (hasil1 == n):   
    print("fungsi p(n) adalah konstan")
else:
    print("fungsi p(n) tidak konstan")