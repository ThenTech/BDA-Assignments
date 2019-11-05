number = (input("number: "))

for i in range(len(number)):
    if int(number[i]) % 2 == 0:
        x = number.count(number[i] % 2 == 0)
        print(x)
        break