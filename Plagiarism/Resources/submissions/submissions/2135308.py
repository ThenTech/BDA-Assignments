Number = input("Give your number: ")
counter = 0
for i in range(len(Number)):
    if int(Number[i]) % 2 == 0:
        counter += 1
print(counter)
