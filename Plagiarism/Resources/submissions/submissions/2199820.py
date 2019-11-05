def dismantle(sentence):
	alphabeticalsymbols = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN"
	letters = 0
	for i in range(len(sentence)):
		if sentence[i] in alphabeticalsymbols:
			letters += 1
			print(sentence[i], end="")
		elif sentence[i] == " " and letters > 0:
			print("", letters)
			letters = 0
	print("", letters)


sentence = input("enter a sentence ")
dismantle(sentence)