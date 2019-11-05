zin = input("")
alfabet = "abcdefghijklmnopqrstuvwxyz"
aantal = 0
for i in range(len(alfabet)):
	for j in range(len(zin)):
		if zin[j] == alfabet[i]:
			aantal += 1
	print(alfabet[i] + ": " + str(aantal))
	aantal = 0
