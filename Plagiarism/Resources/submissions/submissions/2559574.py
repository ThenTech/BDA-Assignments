totaal = int(input("Geef hier je bedrag in eurocent in: "))
munten2euro = totaal//200
totaal = totaal - munten2euro*200
munten1euro = totaal//100
totaal = totaal - munten1euro*100
munten50cent = totaal//50
totaal = totaal - munten50cent*50
munten20cent = totaal//20
totaal = totaal - munten20cent*20
munten10cent = totaal//10
totaal = totaal - munten10cent*10
munten5cent = totaal//5
totaal = totaal - munten5cent*5
munten2cent = totaal//2
totaal = totaal - munten2cent*2
munten1cent = totaal//1
totaal = totaal - munten1cent*1

print("2-euros:", munten2euro)
print("1-euros:", munten1euro)
print("50c-euros:", munten50cent)
print("20c-euros:", munten20cent)
print("10c-euros:", munten10cent)
print("5c-euros:", munten5cent)
print("2c-euros:", munten2cent)
print("1c-euros:", munten1cent)