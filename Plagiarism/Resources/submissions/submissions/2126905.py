iOne = input("")
iTwo = input("")
iFive = input("")
iTen = input("")
iTwenty = input("")

one = int(iOne)
two = int(iTwo) * 2
five = int(iFive) * 5
ten = int(iTen) * 10
twenty = int(iTwenty) * 20

result = (one + two + five + ten + twenty) / 100

print("You have %.2f euro!" % result)