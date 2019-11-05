number = input("Give me a number: ")

even = 0
location = 0

for g in range(len(number)):
    g = int(number[location])
    if g % 2 == 0:
        even += 1
        location += 1
    else:
        even = even
        location += 1
print(even)