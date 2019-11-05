alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sentence1 = input()
sentence2 = input()
anagram = True

for letter in alpha:
    if sentence2.count(letter) != sentence1.count(letter):
        anagram = False
        
if anagram:
    print(sentence1 + " and " + sentence2 + " are anagrams")
else:
    print(sentence1 + " and " + sentence2 + " are not anagrams")