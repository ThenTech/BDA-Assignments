# write your code here
ones1 = input("Number of coins of 1")
twos1 = input("Number of coins of 2")
fives1 = input("Number of coins of 5")
tens1 = input("Number of coins of 10")
twenties1 = input("Number of coins of 20")

ones = int(ones1) * 1 
twos = int(twos1) * 2
fives = int(fives1) * 5 
tens = int(tens1) * 10 
twenties = int(twenties1) * 20

sum = ones + twos + fives + tens + twenties

euros = sum//100
cents = sum%100

print("You have ", euros, ".", cents , " euro!", sep="")

