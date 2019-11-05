number = int(input("give a number: "))

count = 0
while (number > 0):
    n = number % 10

    if n % 2 == 0:
        count += 1
    number = number // 10

print(count)