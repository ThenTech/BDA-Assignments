x = int(input("number?"))
y = int(input("number?"))
F = 1
for i in range(y):
    F = F * (x - i)/(y - i)
print(round(F))