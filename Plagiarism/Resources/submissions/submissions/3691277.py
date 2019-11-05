coins1 = int(input())
coins2 = int(input())
coins5 = int(input())
coins10 = int(input())
coins20 = int(input())

money = coins1 + 2*coins2 + 5*coins5 + 10*coins10 + 20*coins20
euro = money // 100
cent = money % 100

print("You have ", euro, ".", cent, " euro!", sep="")