number = int((input("number: ")))

count = 0

while number != 0:
    digit = number % 2
    if digit == 0:
        count += 1
    number = number // 10
print(count)