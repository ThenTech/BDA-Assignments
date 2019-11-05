amount = int(input("Write here how much you have to pay in cent: "))
twoE = 0
oneE = 0
fiftyC = 0
twentyC = 0
tenC = 0
fiveC = 0
twoC = 0
oneC = 0
while amount / 200 > 1:
    twoE += 1
    amount - 200
while amount / 100 > 1:
    oneE += 1
    amount - 100
while amount / 50 > 1:
    fiftyC += 1
    amount - 50
while amount / 20 > 1:
    twentyC += 1
    amount - 20
while amount / 10 > 1:
    tenC += 1
    amount - 10
while amount / 5 > 1:
    fiveC += 1
    amount - 5
while amount / 2 > 1:
    twoC += 1
    amount - 2
while amount / 1 > 1:
    oneC += 1
    amount - 1
print(twoE,
oneE,
fiftyC,
twentyC,
tenC,
fiveC,
twoC,
oneC)
