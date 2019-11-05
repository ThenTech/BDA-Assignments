def encode(s, n):
	zin = ""
	for i in s:
		if i == " ":
			zin = zin + " "
			continue
			
		elif ord(i) > 96 and ord(i) < 123:
			letter1 = ord(i) + n
			letter = chr(letter1)
			zin = zin + letter

		else:
			letter2 = ord(i) - 26 + n
			letter = chr(letter2)
			zin = zin + letter
	return zin

def decode(s, n):
	zin = ""
	for i in s:
		if i == " ":
			zin = zin + " "
			continue
			
		elif ord(i) > 96 and ord(i) < 123:
			letter1 = ord(i) - n
			letter = chr(letter1)
			zin = zin + letter

		else:
			letter2 = ord(i) - 26 + n
			letter = chr(letter2)
			zin = zin + letter
	return zin