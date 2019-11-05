dayB = int(input("Give birthday day: "))
monthB = int(input("Give birthday month: "))
yearB = int(input("Give birthday year: "))
dayC = int(input("Give current day: "))
monthC = int(input("Give current month: "))
yearC = int(input("Give current year: "))
yearDifference = yearC - yearB
if monthC > monthB:
    yearDifference = yearDifference
elif monthC == monthB:
    if dayC >= dayB:
        yearDifference = yearDifference
    else:
        yearDifference = yearDifference - 1
else:
    yearDifference = yearDifference - 1
print(yearDifference)
