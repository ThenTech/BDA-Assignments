# write your code here
ones1 = input("Number of coins of 1")
twos1 = input("Number of coins of 2")
fives1 = input("Number of coins of 5")
tens1 = input("Number of coins of 10")
twenties1 = input("Number of coins of 20")

ones = int(ones1) * 0.01
twos = int(twos1) * 0.02
fives = int(fives1) * 0.05
tens = int(tens1) * 0.10
twenties = int(twenties1) * 0.20

sum = ones + twos + fives + tens + twenties


print("You have", format(sum, '.2f'), "euro!", sep=" ")

