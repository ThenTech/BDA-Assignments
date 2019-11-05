bDay = int(input())
bMonth = int(input())
bYear = int(input())

cDay = int(input())
cMonth = int(input())
cYear = int(input())

if bDay <= cDay and bMonth <= cMonth:
    print(cYear - bYear)
elif bDay >= cDay and bMonth >= cMonth:
    print(cYear - bYear - 1)