x = input()
y = ""
for i in range(x):
    y += i
if (y is x):
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")