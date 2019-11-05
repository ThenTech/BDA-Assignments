number = str(input())

count = 0
for i in number:
    a = int(i)
    if a % 2 == 0:
        count += 1
print(count)