dag = input("geef het aantal dagen hier")
uur = input("Geef het aantal uren hier")
minuut = (uur * int(uur)) + (60 * 24 * int(dag))
print(minuut)