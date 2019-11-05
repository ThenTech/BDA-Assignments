def removeunlucky(remove, unlickylist):
	newlist = []
	i = 0
	while i < len(unlickylist):
		i += 1
		if i % remove != 0:
			newlist += [unlickylist[i-1]]
	return newlist

def lucky_numbers(n):
	numbers = []
	for i in range(n):
		numbers += [i+1]

	i = 2
	while i <= len(numbers):
		numbers = removeunlucky(i, numbers)
		i += 1
	return numbers