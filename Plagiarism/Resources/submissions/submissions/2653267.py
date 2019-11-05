x = int(input())

a = x // 200
x = x - 200*a
b = x //100
x = x - 100*b
c = x // 50
x = x - 50*c
d = x //20
x = x - 20*d
e = x //10
x = x - 10*e
f = x // 5
x = x - 5*f
g = x // 2
x = x - 2*g
h = x // 1


print("2-euros:", a )
print("1-euros:", b )
print("50c-euros:", c )
print("20c-euros:", d )
print("10c-euros:", e )
print("5c-euros:", f )
print("2c-euros:", g )
print("1c-euros:", h )