year = int(input())
divbyhundred = (year % 100) == 0
divbyfouhundred = (year % 400) == 0
divbyfour = (year % 4) == 0
isleapyear = False

if divbyfour:
    if divbyhundred:
        if divbyfouhundred:
            isleapyear = True
    else:
        isleapyear = True

if isleapyear:
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")
