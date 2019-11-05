number = input("Give a number: ")
count = 0
for i in number:
    if int(i) % 2 == 0:
        count += 1
print(count)
