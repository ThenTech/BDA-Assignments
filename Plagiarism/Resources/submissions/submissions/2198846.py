def convert_to_uppercase(s):
	hoofd = ""
	zin = ""
	for i in s:
		zin = ord(i) - 32
		if zin > 90:
			hoofd = hoofd + chr(zin)
		else:
			hoofd = hoofd + i
	return(hoofd)
