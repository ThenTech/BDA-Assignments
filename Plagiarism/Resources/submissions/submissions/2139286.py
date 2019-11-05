getal =input("give a number: ")
sum = 0
p=0
for l in range(len(getal)):
    i = int(getal[p])
    if i%2 == 0:
         sum = sum + 1
         p = p+1
    else:
        sum = sum
        p = p+1
print(sum)

