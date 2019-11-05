x = input("x")
booly = True
for i in range(len(x)//2):
    if x[i] == x[len(x)-1-i]:
        continue
    else:
        booly = False
        break
if booly == False:
    print(x ,"is not a palindrome")
else:
    print(x, "is a palindrome")