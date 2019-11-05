amount = int(input("Amount: "))
print("2-euros:", str(amount // 200))
amount = amount % 200
print("1-euros:", str(amount // 100))
amount = amount % 100
print("50c-euros:", str(amount // 50))
amount = amount % 50
print("20c-euros:", str(amount // 20))
amount = amount % 20
print("10c-euros:", str(amount // 10))
amount = amount % 10
print("5c-euros:", str(amount // 5))
amount = amount % 5
print("2c-euros:", str(amount // 2))
amount = amount % 2
print("1c-euros:", str(amount // 1))
