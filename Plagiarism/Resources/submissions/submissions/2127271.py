cent1 = input("Hoeveel muntstukken van 1 cent zijn er?")
cent2 = input("Hoeveel muntstukken van 2 cent zijn er?")
cent5 = input("Hoeveel muntstukken van 5 cent zijn er?")
cent10 = input("Hoeveel muntstukken van 10 cent zijn er?")
cent20 = input("Hoeveel muntstukken van 20 cent zijn er?")

sumcent = int(cent1) + (int(cent2)*2) + (int(cent5)*5) + (int(cent10)*10) + (int(cent20)*20)

print("You have " +format(sumcent/100, ".2f") + " euro!")