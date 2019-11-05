a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a = a*1
b = b*2
c = c*5
d = d*10
e = e*20

summ = a + b + c + d + e
x = summ // 100
y = summ % 10
z = summ % 100
z = z*10
z = z % 1
print("You have ", x,".", y, z," euro!", sep ="")