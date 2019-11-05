def is_unique(lsttocheck):
	for i in range(len(lsttocheck)):
		if lsttocheck[i] in lsttocheck[i+1:]:
			return False
	return True
