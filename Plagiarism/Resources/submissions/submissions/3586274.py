onec = int(input())
twoc = int(input())
fivec = int(input())
tenc = int(input())
twentyc = int(input())

total = (onec * 1 + twoc * 2 + fivec * 5 + tenc * 10 + twentyc * 20)

euro = total // 100
a = total % 100
b = a // 10
c = a % 10


print("You have ", euro, ".", b, c, " euro!", sep="")