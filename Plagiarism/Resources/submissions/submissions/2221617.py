x = input("give me a number: ")
count = 0
for i in x:
    if int(i)% 2 == 0:
        count += 1
print(count)