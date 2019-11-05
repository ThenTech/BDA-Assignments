digit = input()
str_digit = str(digit)
digits = 0
for char in str_digit:
    if(int(char) % 2 == 0):
        digits += 1

print(digits)