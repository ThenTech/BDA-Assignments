x = int(input("give an x: "))
y = int(input("give a y: "))

product = 1
for i in range (y):
    product *= (x-i)/(y-i)

print(int(product))