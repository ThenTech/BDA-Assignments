total = int(input("Totaal eurocent: "))

euro2 = total // 200
rest = total % 200

euro1 = rest // 100
rest = rest % 100

eurocent50 = rest // 50
rest = rest % 50

eurocent20 = rest // 20
rest = rest % 20

eurocent10 = rest // 10
rest = rest % 10

eurocent5 = rest // 5
rest = rest % 5

eurocent2 = rest // 2
rest = rest % 2

eurocent1 = rest // 1

print("2-euros:", euro2)
print("1-euros:", euro1)
print("50c-euros:", eurocent50)
print("20c-euros:", eurocent20)
print("10c-euros:", eurocent10)
print("5c-euros:", eurocent5)
print("2c-euros:", eurocent2)
print("1c-euros:", eurocent1)