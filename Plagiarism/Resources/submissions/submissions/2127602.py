#submision one was much cleaner and shorter but the unit tests flagged it as wrong because of trailing zeros in the float
#can't seem to figure out why it isn't executing right. on my pc it works, and the python tutor of the site won't load atm (maintenance on site)
#used a different solution that is a bit easier
coinsOfOne = int(input())
coinsOfTwo = int(input())
coinsOfFive = int(input())
coinsOfTen = int(input())
coinsOfTwenty = int(input())

MoneyOwned = (coinsOfTwenty*20)+(coinsOfTen*10)+(coinsOfFive*5)+(coinsOfTwo*2)+coinsOfOne
eurosOwned = int(MoneyOwned / 100)

centsOwned = int(MoneyOwned - (eurosOwned * 100))

centsTensOwned = int(centsOwned / 10)
centsSingleOwned = int(centsOwned - (centsTensOwned * 10))

outputText = str(eurosOwned) + "." + str(centsTensOwned)

if int(centsSingleOwned) > 0:
    outputText += str(centsSingleOwned)

print("You have ", outputText, " euro!", sep="")