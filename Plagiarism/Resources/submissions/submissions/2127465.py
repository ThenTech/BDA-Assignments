coinsOfOne = int(input())
coinsOfTwo = int(input())
coinsOfFive = int(input())
coinsOfTen = int(input())
coinsOfTwenty = int(input())

CentsOwnedTot = (coinsOfTwenty*20)+(coinsOfTen*10)+(coinsOfFive*5)+(coinsOfTwo*2)+coinsOfOne
eurosOwned = float(CentsOwnedTot) / 100

print("You have ", eurosOwned, " euro!", sep="")