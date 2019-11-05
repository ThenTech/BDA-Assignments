x = input("")
y = x
z = True
for i in range(len(x)-1):
    if (x[i] != y[len(x)-i-1]):
        z = False
        break
if z:
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")