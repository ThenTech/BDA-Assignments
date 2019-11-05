# write your code here

cent_1 = int(input("How many coins of 1 eurocents do you have?"))
cent_2 = int(input("How many coins of 2 eurocents do you have?"))
cent_5 = int(input("How many coins of 5 eurocents do you have?"))
cent_10 = int(input("How many coins of 10 eurocents do you have?"))
cent_20 = int(input("How many coins of 20 eurocents do you have?"))

money = cent_1 * 0.01 + cent_2 * 0.02 + cent_5 * 0.05 + cent_10 * 0.1 + cent_20 * 0.2

print("You have ",money , " euro!", sep="")