def convert_to_uppercase(s):
	hoofd = ""
	zin = ""
	for i in s:
		zin = ord(i)
		if zin > 96:
			zin = ord(i) - 32
			hoofd = hoofd + chr(zin)
		else:
			hoofd = hoofd + i
	return(hoofd)