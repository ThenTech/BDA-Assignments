number = input("Give me a number: ")

even = 0

for g in range(len(number)):
    if int(number[g]) % 2 == 0:
        even += 1

print(even)