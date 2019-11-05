word1 = input()
word2 = input()
word1_modified = word1
anagram_found = True
counter = 0
for char_w2 in word2:
    if char_w2 in word1_modified:
        word1_modified = word1_modified.replace(char_w2, '', 1)
    else:
        anagram_found = False

if anagram_found:
    print(word1, "and", word2, "are anagrams")
else:
    print(word1, "and", word2, "are not anagrams")


word1 = input()
word2 = input()
word1_modified = word1
anagram_found = True
counter = 0
for char_w2 in word2:
    if char_w2 in word1_modified:
        word1_modified = word1_modified.replace(char_w2, '', 1)
    else:
        anagram_found = False

if anagram_found:
    print(word1, "and", word2, "are anagrams")
else:
    print(word1, "and", word2, "are not anagrams")

