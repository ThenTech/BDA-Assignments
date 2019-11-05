amount = int(input("Write here how much you have to pay in cent: "))
twoE = 0
oneE = 0
fiftyC = 0
twentyC = 0
tenC = 0
fiveC = 0
twoC = 0
oneC = 0
while (amount / 200) >= 1:
    twoE += 1
    amount -= 200
    if amount < 1:
        break
while (amount / 100) >= 1:
    oneE += 1
    amount -= 100
    if amount < 1:
        break
while (amount / 50) >= 1:
    fiftyC += 1
    amount -= 50
    if amount < 1:
        break
while amount / 20 >= 1:
    twentyC += 1
    amount -= 20
    if amount < 1:
        break
while amount / 10 >= 1:
    tenC += 1
    amount -= 10
    if amount < 1:
        break
while amount / 5 >= 1:
    fiveC += 1
    amount -= 5
    if amount < 1:
        break
while amount / 2 >= 1:
    twoC += 1
    amount -= 2
    if amount < 1:
        break
while amount / 1 >= 1:
    oneC += 1
    amount -= 1
    if amount < 1:
        break

print("2-euros: ", twoE)
print("1-euros: ", oneE)
print("50c-euros ", fiftyC)
print("20c-euros ", twentyC)
print("10c-euros ", tenC)
print("5c-euros ", fiveC)
print("2c-euros ", twoC)
print("1c-euros ", oneC)