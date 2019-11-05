word1 = input('Word?')
word2 = input('Word 2?')
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = len(word1) - 1
q = 0
w = 0
anagram = True
for k in range(len(alphabet)):
    while i >= 0:
        if word1[i] == alphabet[k]:
            q += 1
        if word2[i] == alphabet[k]:
            w += 1
        i -= 1
    if w != q:
        print(word1, 'and', word2, 'are not anagrams')
        anagram = False
        break
    i = len(word1) - 1
    q = 0
    w = 0
if anagram == True:
    print(word1, 'and', word2, 'are anagrams')
