one = int(input())
two = 2*int(input())
five = 5*int(input())
ten = 10*int(input())
twenty = 20*int(input())
total = one + two + five + ten + twenty

print("You have ", total//100, ".", total%100//10, total%10, " euro!", sep="")