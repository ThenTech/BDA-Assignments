#appologies, i realized yesterday that i read the requirements backwards
coinsOfOne = int(input())
coinsOfTwo = int(input())
coinsOfFive = int(input())
coinsOfTen = int(input())
coinsOfTwenty = int(input())

MoneyOwned = (coinsOfTwenty*20)+(coinsOfTen*10)+(coinsOfFive*5)+(coinsOfTwo*2)+coinsOfOne
eurosOwned = MoneyOwned / 100

outputText = "%.2f" % eurosOwned

print("You have ", outputText, " euro!", sep="")