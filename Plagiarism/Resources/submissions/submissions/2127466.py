cent_1=int(input("Hoeveel munten van 1 cent?"))
cent_2=int(input("Hoeveel munten van 2 cent?"))
cent_5=int(input("Hoeveel munten van 5 cent?"))
cent_10=int(input("Hoeveel munten van 10 cent?"))
cent_20=int(input("Hoeveel munten van 20 cent?"))
totaal=cent_1+cent_2+cent_5+cent_10+cent_20
print("You have ",totaal//100,".",totaal//10%10,totaal%10," euro!",sep="")