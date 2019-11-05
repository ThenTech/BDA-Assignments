
y = int(input("give an y: "))

product2 = 1
sum = 0
for i in range(y):
    product2 *= (i+1)
    sum += product2

print(sum)