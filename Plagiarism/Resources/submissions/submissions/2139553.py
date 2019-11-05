string = input("")

aantal = 0
for i in range(0, len(string)):
	if (int(string[i]) % 2) == 0:
		aantal += 1

print(aantal)
