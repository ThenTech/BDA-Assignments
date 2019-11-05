Word1 = input("Give the first word: ")
Word1Replace = Word1.replace(" ", "")
Word2 = input("Give the second word: ")
Word2Replace = Word2.replace(" ", "")
Word1Sort = sorted(Word1Replace)
Word2Sort = sorted(Word2Replace)

if Word1Sort == Word2Sort:
    print(Word1, "and", Word2, "are anagrams")
else:
    print(Word1, "and", Word2, "are not anagrams")
