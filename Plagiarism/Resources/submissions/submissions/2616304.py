s = input("give string: ")
b = input("give string: ")

alfabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alfabet:
    count = ""
    for i in s:
        if letter == i:
            count += letter
        else:
            count = count

for letter in alfabet:
    count2 = ""
    for i in b:
        if letter == i:
            count2 += letter
        else:
            count2 = count2

if count == count2:
    print(s, "and", b, "are anagrams")
else:
    print(s, "and", b, "are not anagrams")


