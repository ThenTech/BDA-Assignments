s = input("give string: ")
b = input("give string: ")

alfabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alfabet:
    count = 0
    for i in s:
        if letter == i:
            count += 1
        else:
            count = count

for letter in alfabet:
    count2 = 0
    for i in b:
        if letter == i:
            count2 += 1
        else:
            count2 = count2

if count == count2:
    print(s, "and", b, "are anagrams")
else:
    print(s, "and", b, "are not anagrams")


