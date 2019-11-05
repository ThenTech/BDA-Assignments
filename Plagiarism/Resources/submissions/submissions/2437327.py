getal = int(input("Geef een getal: "))
factorial = 1
factorial_sum = 0 
for i in range(getal):
    for j in range(i):
        factorial *= j + 1
    factorial_sum += factorial
    factorial = 1
print(factorial_sum)