price = input("Amount to be payed = ")
price = int(price)

two_euro = price // 200
remaining = price % 200

one_euro = remaining // 100
remaining = remaining % 100

fifty_cent = remaining // 50
remaining = remaining % 50

twenty_cent = remaining // 20
remaining = remaining % 20

ten_cent = remaining // 10
remaining = remaining % 10

five_cent = remaining // 5
remaining = remaining % 5

two_cent = remaining // 2
remaining = remaining % 2

one_cent = remaining // 1

print("2-euros:", two_euro)
print("1-euros:", one_euro)
print("50c-euros:", fifty_cent)
print("20c-euros:", twenty_cent)
print("10c-euros:", ten_cent)
print("5c-euros:", five_cent)
print("2c-euros:", two_cent)
print("1c-euros:", one_cent)