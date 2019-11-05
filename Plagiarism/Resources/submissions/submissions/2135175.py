x = input("")
count = 0

for i in range(0, len(x)):
    if int(x[i]) % 2 == 0:
        count += 1

print(count)