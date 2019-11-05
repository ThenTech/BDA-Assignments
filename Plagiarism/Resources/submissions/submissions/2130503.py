# write your code here
getal = int(input("geef een getal groter dan 0: "))
result = 1
sumResult = 0

for i in range(1, getal + 1):
    result = 1
    for j in range(1, i + 1):
        result *= j
    sumResult += result

print(sumResult)
