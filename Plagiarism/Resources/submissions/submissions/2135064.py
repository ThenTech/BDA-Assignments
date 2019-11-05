number = input()
counter = 0

for x in range(len(number)):
    curr = int(number[x])
    if (curr % 2) == 0:
        counter += 1

print(str(counter))