x = input()
y = ""
for i in range(len(x)):
    y += x[i]
if (y is x):
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")