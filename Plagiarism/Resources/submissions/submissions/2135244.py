x = input("word?")

for i in range(len(x)):
    if i+1 != len(x):
        if x[len(x)-1-i] == x[i]:
            continue
        else:
            print(x, "is not a palindrome")
            break
    else:
        print(x, "is a palindrome")