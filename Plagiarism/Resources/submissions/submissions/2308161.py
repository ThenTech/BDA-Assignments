a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

f = a * 1
g = b * 2
h = c * 5
i = d * 10
j = e * 20

n = (f+g+h+i+j) // 100
m = ((f+g+h+i+j) % 100) // 10
o = ((f+g+h+i+j) % 10)

print("You have ", n,".", m, o, " euro!", sep ="")