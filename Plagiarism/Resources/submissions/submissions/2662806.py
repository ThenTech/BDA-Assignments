# write your code here
x = input('number')
x = int(x)
som = 0
for i in range (1, (x + 1)):
    for j in range(1, (i + 1)):
        som = som + j
print(som)