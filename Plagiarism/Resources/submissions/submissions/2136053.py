string1 = input()
string2 = input()
anagram = True
for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    amount1 = 0
    amount2 = 0
    pos = 0
    while pos < len(string1):
        if string1[pos] == letter:
            amount1 += 1
        pos += 1
    pos = 0
    while pos < len(string2):
        if string2[pos] == letter:
            amount2 += 1
        pos += 1
    if amount1 != amount2:
        anagram = False
if anagram:
    print(string1, "and", string2, "are anagrams")
else:
    print(string1, "and", string2, "are not anagrams")