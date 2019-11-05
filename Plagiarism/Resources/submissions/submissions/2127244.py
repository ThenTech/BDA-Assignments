# write your code here
a1 = int(input())
a2 = int(input())
a5 = int(input())
a10 = int(input())
a20 = int(input())
sum = a1 * 1 + a2 * 2 + a5 * 5 + a10 * 10 + a20 * 20
x = sum // 100
y = sum // 10 % 10
z = sum % 10
print("You have ", x , '.', y , z, " euro!", sep = "" )