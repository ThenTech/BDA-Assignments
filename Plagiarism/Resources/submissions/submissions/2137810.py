woord = input("")
palindrome = ""
for i in range(len(woord), 0, -1):
	palindrome += woord[i - 1]
	
if palindrome == woord:
	print(woord, "is a palindrome")
else:
	print(woord,"is not a palindrome")
