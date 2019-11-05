def removeunlucky(removemultsof, unlickylist):
	newlist = []
	for i in unlickylist:
		if i % removemultsof != 0:
			newlist += [i]
	return newlist

def lucky_numbers(n):
	numbers = []
	for i in range(n):
		numbers += [i+1]
	print(numbers)

	removemultsof = 2

	while removemultsof <= numbers[len(numbers)-1]:
		numbers = removeunlucky(removemultsof, numbers)
		removemultsof += 1
		print(numbers)