w = input("Give a string ")

mirror = ""

for i in range(0, len(w)):
    mirror = w[i] + mirror

if w == mirror:
    print(w, "is a palindrome")
else:
    print(w, "is not a palindrome")
