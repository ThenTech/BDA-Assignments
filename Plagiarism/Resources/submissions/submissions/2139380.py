Day1 = int(input("Give the start day: "))
Month1 = int(input("Give the start month: "))
Year1 = int(input("Give the start year: "))
Day2 = int(input("Give the end day: "))
Month2 = int(input("Give the end month: "))
Year2 = int(input("Give the end year: "))
DayCounter = 0
MonthCounter = 0
YearCounter = 0


while True:
    DayCounter += 1
    if DayCounter == 31:
        DayCounter = 0
        MonthCounter += 1
    if MonthCounter == 12:
        MonthCounter = 0
        YearCounter += 1
    if (Year1 + YearCounter) == Year2:
        break
if Month1 > Month2:
    print(YearCounter - 1)
else:
    print(YearCounter)
