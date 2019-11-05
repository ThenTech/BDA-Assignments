number_string = input("Give a number ")

even_digits = 0
for digit in number_string:
    if int(digit) % 2 == 0:
        even_digits += 1
print(even_digits)
