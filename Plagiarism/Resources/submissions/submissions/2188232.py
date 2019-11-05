x = input("word?")
i = 0
ln_x = len(x)//2
a = True


for i in range(ln_x):
    if x[i] != x[len(x)-1-i] and a == True:
        a = False

if a == True:
    print(x, "is a palindrome")
else:
    print(x, "is not a palindrome")





