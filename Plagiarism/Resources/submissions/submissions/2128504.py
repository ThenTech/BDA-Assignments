aantalDagen = int(input("Vul het aantal dagen in: "))
aantalUren = int(input("Vul het aantal uren in: "))

dagenInUren = aantalDagen * 24
aantalUren = dagenInUren + aantalUren
urenInMinuten = aantalUren * 60

print("Dat zijn ", urenInMinuten, " minuten!")