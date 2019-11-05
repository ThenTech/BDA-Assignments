total = int(input("Total (in eurocents): "))

types_of_coin = [200, 100, 50, 20, 10, 5, 2, 1]
amount_of_coin = [0, 0, 0, 0, 0, 0, 0, 0]

type_of_coin_string = ["2-euros", "1-euros", "50c-euros", "20c-euros", "10c-euros", "5c-euros", "2c-euros", "1c-euros"]

i = 0

while total > 0:
    if total >= types_of_coin[i]:
        remainder_of_total = total % types_of_coin[i]
        amount_of_coin[i] = round((total - remainder_of_total) / types_of_coin[i])
        total = remainder_of_total
    else:
        i += 1

for x in range(len(types_of_coin)):
    print("{c_type}: {c_amount}".format(
        c_type=type_of_coin_string[x],
        c_amount=amount_of_coin[x]
    ))
