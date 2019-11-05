x = int(input(""))

euro2 = x // 200
x = x - (euro2 * 200)
euro1 = x // 100
x = x - (euro1 * 100)
cent50 = x // 50
x = x - (cent50 * 50)
cent20 = x // 20
x = x - (cent20 * 20)
cent10 = x // 10
x = x - (cent10 * 10)
cent5 = x // 5
x = x - (cent5 * 5)
cent2 = x // 2
x = x - (cent2 * 2)
cent1 = x // 1
x = x - (cent1 * 1)

print("2-euros: ", euro2)
print("1-euros: ", euro1)
print("50c-euros: ", cent50)
print("20c-euros: ", cent20)
print("10c-euros: ", cent10)
print("5c-euros: ", cent5)
print("2c-euros: ", cent2)
print("1c-euros: ", cent1)