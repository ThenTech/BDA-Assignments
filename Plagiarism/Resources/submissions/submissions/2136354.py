number = input("Number: ")
even_digit_count = 0

for digit in number:
    if int(digit) % 2 == 0:
        even_digit_count += 1

print(even_digit_count)
