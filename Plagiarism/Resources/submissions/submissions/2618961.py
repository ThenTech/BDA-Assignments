nucleobasen = ["A","C","G","T"]
mogelijkheid = ""
def alle_nucleobasen(n):
    global mogelijkheid
    for i in nucleobasen:
        mogelijkheid += i
        if len(mogelijkheid) == n:
            print(mogelijkheid)

        if len(mogelijkheid) != n:
            volgende(mogelijkheid, n)
            mogelijkheid = ""
        mogelijkheid = ""

def volgende(mogelijkheid, n):
    for i in nucleobasen:
        if len(mogelijkheid+i) == n:
            print(mogelijkheid+i)
        else:
            volgende(mogelijkheid+i, n)

alle_nucleobasen(int(input()))