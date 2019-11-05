a = int(input("aantal munten van 1 cent: "))
b = int(input("aantal munten van 2 cent: "))
c = int(input("aantal munten van 5 cent: "))
d = int(input("aantal munten van 10 cent: "))
e = int(input("aantal munten van 20 cent: "))
f = a+2*b+5*c+10*d+20*e
g = f//100
h = f%100
t = h//10
i = h%10
print("You have", g, ".", t, i "euro!")