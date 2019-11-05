s = input("give string: ")
b = input("give string: ")
count = ""
alfabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alfabet:

    for i in s:
        if letter == i:
            count += letter
        else:
            count = count
count2 = ""
for letter in alfabet:

    for i in b:
        if letter == i:
            count2 += letter
        else:
            count2 = count2


if count == count2:
    print(s, "and", b, "are anagrams")
    print(count, count2)
else:
    print(s, "and", b, "are not anagrams")
    print(count, count2)


