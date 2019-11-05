zin = input("")
anagram = input("")
alfabet = "abcdefghijklmnopqrstuvwxyz"
aantalzin = 0
aantalanagram = 0
for i in range(len(alfabet)):
	for j in range(0, len(zin)):
		if zin[j] == alfabet[i]:
			aantalzin += 1
#	print(alfabet[i] + ": " + str(aantalzin))
	aantalzin = 0

		if anagram[j] == alfabet[i]:
			aantalanagram += 1
#	print(alfabet[i] + ": " + str(aantalanagram))
	aantalanagram = 0

		if aantalanagram != aantalzin:
			print(zin + "and" + anagram + "are anagrams")
		else:
			print(zin + "and" + anagram + "are not anagrams")