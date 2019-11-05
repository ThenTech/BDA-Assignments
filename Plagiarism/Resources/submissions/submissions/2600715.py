dag = int(input("Geef de aantal dagen: "))
uren = int(input("Geef de aantal ure: "))

dag = dag *24*60
uren= uren *60
minuten = dag +uren

print(minuten)