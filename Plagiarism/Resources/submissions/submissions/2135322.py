number = input(" ")
x = 0
count = 0
while x < len(number):
    if (int(number[x]) % 2) == 0:
        count += 1
    x += 1
print(count)