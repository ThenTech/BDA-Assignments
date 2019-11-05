number = input("Give a number: ")
even = 0

for digit in number:
    digit_2 = int(digit)
    if digit_2 % 2 == 0:
        even += 1
print(even)
