amount_of_money = int(input("give an amount of money (in eurocents): "))

amount_of_money_left = amount_of_money
two_euro = amount_of_money//200
amount_of_money_left = amount_of_money_left - two_euro*200
one_euro = amount_of_money_left//100
amount_of_money_left = amount_of_money_left - one_euro*100
fifty_cents = amount_of_money_left//50
amount_of_money_left = amount_of_money_left - fifty_cents*50
twenty_cents = amount_of_money_left//20
amount_of_money_left = amount_of_money_left - twenty_cents*20
ten_cents = amount_of_money_left//10
amount_of_money_left = amount_of_money_left - ten_cents*10
five_cents = amount_of_money_left//5
amount_of_money_left = amount_of_money_left - five_cents*5
two_cents =amount_of_money_left//2
amount_of_money_left = amount_of_money_left - two_cents*2
one_cents = amount_of_money_left

print("2-euros:" , two_euro)
print("1-euros:" , one_euro)
print("50c-euros:" , fifty_cents)
print("20c-euros:" , twenty_cents)
print("10c-euros:" , ten_cents)
print("5c-euros: " , five_cents)
print("2c-euros: " , two_cents)
print("1c-euros: " , one_cents)