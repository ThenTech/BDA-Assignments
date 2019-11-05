x = input("x")
s = ""
for i in range(len(x)):
    s += x[len(x)-i-1]
print(s)