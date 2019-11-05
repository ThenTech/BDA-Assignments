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
summ = summ - x *100
y = summ // 10
summ = summ - x*10
z = summ
print("You have ", x,".", z, y," euro!", sep ="")