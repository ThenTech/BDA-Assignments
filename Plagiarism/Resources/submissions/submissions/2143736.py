BDay = int(input())
BMonth = int(input())
BYear = int(input())

CDay = int(input())
CMonth = int(input())
CYear = int(input())

yearsOld = abs(CYear - BYear) - 1

if CMonth > BMonth:
    yearsOld += 1
elif CMonth == BMonth and CDay > BDay:
    yearsOld += 1

print(yearsOld)
