x = input("")
y = x
for i in range(len(x)-1):
    if (x[i] == y[len(x)-i-1]):
        continue
    else:
        print(x, "is not a palindrome")
        break
    print(x, "is a palindrome")