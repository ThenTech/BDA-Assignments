x = input("Geef een woord: ")
i = 0
while i < len(x):
    if x[i] != x[len(x) - 1 - i]:
        print(x, "is not a palindrome")
        break
    elif x[i] == x[len(x)- 1 - i]:
        i = i+1
    if i == len(x) - 1:
        print(x, "is not a palindrome")