comp = 0

day1 = int(input("Geef de dag van je verjaardag in : "))
month1 = int(input("Geef de maand van je verjaardag in : "))
year1 = int(input("Geef het jaar van je verjaardag in : "))

day2 = int(input("Geef de dag de huidige dag in : "))
month2 = int(input("Geef de maand van de huidige dag in : "))
year2 = int(input("Geef het jaar van de hudige dag in : "))

year = int(year2) - int(year1)

if month2 < month1:
    print(year - 1)
elif month2 == month1:
    if day2 < day1:
        print(year-1)
    else:
        print(year)
else:
    print(year)
    