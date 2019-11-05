def print_combos(previous, n):
	if n < 1:
		for i in "ACGT":
			print(previous + i)
	else:
		for nucleo in "ACGT":
			print_combos(previous + nucleo, n-1)


bases = int(input("bases = "))-1
print_combos("",  bases)