input = input()
even = 0

for i in range(len(input)):
    if int(input[i]) % 2 == 0:
        even += 1
print(even)