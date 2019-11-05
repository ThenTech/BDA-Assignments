s = input("Give a string: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count += 1
    print(char, ": ", count, sep="")
