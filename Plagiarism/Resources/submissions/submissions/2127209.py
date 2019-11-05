# write your code here

cent_1 = int(input("How many coins of 1 eurocents do you have?"))
cent_2 = int(input("How many coins of 2 eurocents do you have?"))
cent_5 = int(input("How many coins of 5 eurocents do you have?"))
cent_10 = int(input("How many coins of 10 eurocents do you have?"))
cent_20 = int(input("How many coins of 20 eurocents do you have?"))

money = cent_1 * 1 + cent_2 * 2 + cent_5 * 5 + cent_10 * 10 + cent_20 * 20

Euro = money//100
cents_10 = (money - Euro*100)//10
cents_1 = (money - Euro*100 - cents_10*10)

print("You have ", Euro, ".", cents_10, cents_1, " euro!", sep="")