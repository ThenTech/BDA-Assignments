getal = int(input("Geef een getal: "))
factorial = 1
factorial_sum = 0
for i in range(getal):
    for j in range(getal):
        factorial *= j + 1
    factorial_sum += int(factorial)
print(factorial_sum)