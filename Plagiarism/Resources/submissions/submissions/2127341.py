# write your code here
a = int(input())
res = a
a = int(input())
res += a * 2

a = int(input())
res += a * 5

a = int(input())
res += a * 10

a = int(input())
res += a * 20

print("You have ", res // 100, ".", res % 100, " euro!", sep="")
