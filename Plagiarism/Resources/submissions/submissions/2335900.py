cents = int(input("money: "))
two = cents // 200
cents2 = cents % 200
one = cents2 // 100
cents3 = cents2 % 100
fifty = cents3 // 50
cents4 = cents3 % 50
twenty = cents4 // 20
cents5 = cents4 % 20
ten = cents5 // 10
cents6 = cents5 % 10
five = cents6 // 5
cents7 = cents6 % 5
two2 = cents7 // 2
cents8 = cents7 % 2
one2 = cents8 // 1

print("2-euros:", two)
print("1-euros:", one)
print("50c-euros:", fifty)
print("20c-euros:", twenty)
print("10c-euros:", ten)
print("5c-euros:", five)
print("2c-euros:", two2)
print("1c-euros:", one2)