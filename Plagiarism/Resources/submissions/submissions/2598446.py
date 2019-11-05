total = int(input("total"))
e2 = total // 200
total = total % 200
e1 = total // 100
total = total % 100
c50 = total // 50
total = total % 50
c20 = total // 20
total = total % 20
c10 = total // 10
total = total % 10
c5 = total // 5
total = total % 5
c2 = total // 2
total = total % 2
c1 = total

print("2-euros:", e2)
print("1-euros:", e1)
print("50c-euros:", c50)
print("20c-euros:", c20)
print("10c-euros:", c10)
print("5c-euros:", c5)
print("2c-euros:", c2)
print("1c-euros:", c1)