#submision one was much cleaner and shorter but the unit tests flagged it as wrong because of trailing zeros in the float

coinsOfOne = int(input())
coinsOfTwo = int(input())
coinsOfFive = int(input())
coinsOfTen = int(input())
coinsOfTwenty = int(input())

CentsOwnedTot = (coinsOfTwenty*20)+(coinsOfTen*10)+(coinsOfFive*5)+(coinsOfTwo*2)+coinsOfOne
eurosOwned = int(CentsOwnedTot / 100)
centsTensOwned = int(CentsOwnedTot % 100 / 100)
centsSingleOwned = int(CentsOwnedTot % 100 % 10)

outputText = str(eurosOwned) + "." + str(centsTensOwned)

if int(centsSingleOwned) > int(0):
    outputText += str(centsSingleOwned)

print("You have ", outputText, " euro!", sep="")