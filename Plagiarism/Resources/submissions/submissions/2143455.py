X = str(input("Give a word "))
for i in range(len(X)):
    X[i]
if X[i] == X[len(X) - (i + 1)]:
    print(X, "is a palindrome")
else:
    print(X, "is not a palindrome")