cents_to_pay = int(input("Total value to be paid: "))
two_euros = cents_to_pay // 200
two_euros_rest = cents_to_pay % 200

one_euros = two_euros_rest // 100
one_euros_rest = two_euros_rest % 100

fifty_cents = one_euros_rest // 50
fifty_cents_rest = one_euros_rest % 50

twenty_cents = fifty_cents_rest // 20
twenty_cents_rest = fifty_cents_rest % 20

ten_cents = twenty_cents_rest // 10
ten_cents_rest = twenty_cents_rest % 10

five_cents = ten_cents_rest // 5
five_cents_rest = ten_cents_rest % 5

two_cents = five_cents_rest // 2
two_cents_rest = five_cents_rest % 2

one_cents = two_cents_rest // 1
one_cents_rest = two_cents_rest % 1

print("2-euros:", two_euros)
print("1-euros:", one_euros)
print("50c-euros:", fifty_cents)
print("20c-euros:", twenty_cents)
print("10c-euros:", ten_cents)
print("5c-euros:", five_cents)
print("2c-euros:", two_cents)
print("1c-euros:", one_cents)
