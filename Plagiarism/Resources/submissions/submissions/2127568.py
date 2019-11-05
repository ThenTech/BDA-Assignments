amount = int(input())

eurosAmount = int(amount/100)
centsAmount = int(amount % 100)

twoEuroCoins = int(eurosAmount / 2)
oneEuroCoins = int(eurosAmount % 2)

fiftyCentCoins = int(centsAmount / 50)
twentyCentCoins = int(centsAmount % 50 / 20)
tenCentCoins = int(centsAmount % 50 % 20 / 10)
fiveCentCoins = int(centsAmount % 50 % 20 % 10 / 5)
twoCentCoins = int(centsAmount % 50 % 20 % 10 % 5 / 2)
oneCentCoins = int(centsAmount % 50 % 20 % 10 % 5 % 2)

print("2-euros: ", twoEuroCoins, sep="")
print("1-euros: ", oneEuroCoins, sep="")
print("50c-euros: ", fiftyCentCoins, sep="")
print("20c-euros: ", twentyCentCoins, sep="")
print("10c-euros: ", tenCentCoins, sep="")
print("5c-euros: ", fiveCentCoins, sep="")
print("2c-euros: ", twoCentCoins, sep="")
print("1c-euros: ", oneCentCoins, sep="")