nucleobasen = ["A","C","G","T"]
mogelijkheid = ""
def alle_nucleobasen(n):
    global mogelijkheid
    for i in nucleobasen:
        mogelijkheid += i
        if len(mogelijkheid) != n:
            volgende(mogelijkheid, n)
            mogelijkheid = ""

def volgende(mogelijkheid, n):
    for i in nucleobasen:
        if len(mogelijkheid+i) == n:
            print(mogelijkheid+i)
        else:
            mogelijkheid += i
            volgende(mogelijkheid, n)

alle_nucleobasen(input())