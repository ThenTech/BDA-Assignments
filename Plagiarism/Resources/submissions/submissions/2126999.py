# write your code here
cent_1 = int(input("Amount of 1 Cent coins: "))
cent_2 = int(input("Amount of 2 Cent coins: "))
cent_5 = int(input("Amount of 5 Cent coins: "))
cent_10 = int(input("Amount of 10 Cent coins: "))
cent_20 = int(input("Amount of 20 Cent coins: "))

sum = (cent_1 + 2 * cent_2 + 5 * cent_5 + 10 * cent_10 + 20 * cent_20) / 100
sum = 0.00 + sum

print("You have", sum, "euro!")