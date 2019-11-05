amount = 0
amount2 = 0
word1 = input()
word2 = input()
i = 0
for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
    while i < len(word1):
        if word1[i] == letter:
            amount += 1
        i += 1
    i = 0
    
    while i2 < len(word2):
        if word2[i2] == letter:
            amount2 += 1
        i2 += 1
    i2 = 0
    if amount == amount2:
        amount = 0
        amount2 = 0
        continue
    else:
        break
if amount != amount2:
    print(word1 + " and " + word2 + " are not anagrams")
else:
    print(word1 + " and " + word2 + " are anagrams")
    
    
    