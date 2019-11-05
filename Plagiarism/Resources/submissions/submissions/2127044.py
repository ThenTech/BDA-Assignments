# write your code here
amount_to_pay = int(input("Amount to pay:"))

euro_2 = amount_to_pay // 200
remaining = amount_to_pay - (euro_2 * 200)
euro_1 = remaining // 100
remaining = remaining - (euro_1 * 100)
cent_50 = remaining // 50
remaining = remaining - (cent_50 * 50)
cent_20 = remaining // 20
remaining = remaining - (cent_20 * 20)
cent_10 = remaining // 10
remaining = remaining - (cent_10 * 10)
cent_5 = remaining // 5
remaining = remaining - (cent_5 * 5)
cent_2 = remaining // 2
remaining = remaining - (cent_2 * 2)
cent_1 = remaining
remaining = remaining - (cent_1 * 1)

if remaining == 0:
    print("error")
    print("2-euros:", euro_2)
    print("1-euros:", euro_1)
    print("50c-euros:", cent_50)
    print("20c-euros:", cent_20)
    print("10c-euros:", cent_10)
    print("5c-euros:", cent_5)
    print("2c-euros:", cent_2)
    print("1c-euros:", cent_1)

elif remaining != 0:
    print("error")

