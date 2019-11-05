phrase1 = input("enter phrase 1: ")
phrase2 = input("enter phrase 2: ")
backup = phrase2
anagram = True
for i in range(len(phrase1)):
	letterfound = False
	for j in range(len(phrase2)):
		if phrase1[i] == phrase2[j]:
			letterfound = True
			phrase2 = phrase2[:j] + "." + phrase2[(j+1):]
			break
	if letterfound == False:
		anagram = False
		break
if anagram == True:
	print(phrase1, "and", backup, "are anagrams")
else:
	print(phrase1, "and", backup, "are not anagrams")