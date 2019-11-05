s = input()

result = 0
for x in s:
    if int(x) % 2 == 0:
        result += 1

print(result)