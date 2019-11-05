# write your code here
x = input("word?")

for i in range(len(x)):
    if x[len(x)-1-i] == x[i]:
        print(x, "is a palindrome")
        break
    else:
        print(x, "is not a palindrome")
        break