x = input("")

i = 0

while i < len(x):
    if x[i] != x[len(x) - 1 - i]:
        print(x, 'is not a palindrome')
    elif i == len(x) - 1:
        print(x, "is a palindrome")
    i += 1