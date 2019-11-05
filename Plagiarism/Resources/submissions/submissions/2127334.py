amount = int(input())

e2 = amount//200
amount = amount%200
print("2-euros:", e2)

e1 = amount//100
amount = amount%100
print("1-euros:", e1)

c50 = amount//50
amount = amount%50
print("50c-euros:", c50)

c20 = amount//20
amount = amount%20
print("20c-euros:", c20)

c10 = amount//10
amount = amount%10
print("10c-euros:", c10)

c5 = amount//5
amount = amount%5
print("5c-euros:", c5)

c2 = amount//2
amount = amount%2
print("2c-euros:", c2)

c1 = amount
print("1c-euros:", c1)