x = int(input("Geef een integer op: "))
def base_maker(n, combinatie):
    basen = "ACGT"
    if len(combinatie) == n:
        print(combinatie)
    else:
        for k in basen:
            base_maker(n, combinatie + k)

base_maker(x, "")