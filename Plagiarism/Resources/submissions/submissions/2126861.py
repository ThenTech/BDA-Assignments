money = float(input("Please enter an amount of cents: "))
e2 = 0
e1 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0
while money >= 200:
    money = money -200
    e2 = e2 + 1
while money >= 100:
    money = money -100
    e1 = e1 + 1
while money >= 50:
    money = money -50
    c50 = c50 + 1
while money >= 20:
    money = money -20
    c20 = c20 + 1
while money >= 10:
    money = money -10
    c10 = c10 + 1
while money >= 5:
    money = money -5
    c5 = c5 + 1
while money >= 2:
    money = money -2
    c2 = c2 + 1
while money >= 1:
    money = money -1
    c1 = c1 + 1
print("2-euros:", e2)
print("1-euros:", e1)
print("50c-euros:", c50)
print("20c-euros:", c20)
print("10c-euros:", c10)
print("5c-euros:", c5)
print("2c-euros:", c2)
print("1c-euros:", c1)
