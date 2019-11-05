coins = int(input("Hoeveel munten van 1 cent heb je? "))
coins = coins + int(input("Hoeveel munten van 2 cent heb je? "))
coins = coins + int(input("Hoeveel munten van 5 cent heb je? "))
coins = coins + int(input("Hoeveel munten van 10 cent heb je? "))
coins = coins + int(input("Hoeveel munten van 20 cent heb je? "))

euros = coins//100
aantalCent = coins % 100
tiendesCent = aantalcent // 10
honderdstenCent = antalcent % 10

print("You have ", euros, ".", tiendesCent, honderstenCent, " euro!", sep="")