x = input("")

k = 0
count = 0

while k < len(x):
    if int(x[k]) % 2 == 0:
        count += 1
    k += 1
print(count)