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

print("2-euros: ", twoEuroCoins)
print("1-euros: ", oneEuroCoins)
print("50c-euros: ", fiftyCentCoins)
print("20c-euros: ", twentyCentCoins)
print("10c-euros: ", tenCentCoins)
print("5c-euros: ", fiveCentCoins)
print("2c-euros: ", twoCentCoins)
print("1c-euros: ", oneCentCoins)