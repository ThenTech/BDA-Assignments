coins_1 = int(input("How many coins of 1 eurocents do you have:"))
coins_2 = int(input("How many coins of 2 eurocents do you have:"))
coins_5 = int(input("How many coins of 5 eurocents do you have:"))
coins_10 = int(input("How many coins of 10 eurocents do you have:"))
coins_20 = int(input("How many coins of 20 eurocents do you have:"))

sum_of_cents = (coins_1 * 1) + (coins_2 * 2) + (coins_5 * 5) + (coins_10 * 10) + (coins_20 * 20)
euros = sum_of_cents // 100
eurocents = (sum_of_cents % 100) // 10
cents = (sum_of_cents % 10)


print("You have ",euros, ".", eurocents, cents, " euro!", sep="" )