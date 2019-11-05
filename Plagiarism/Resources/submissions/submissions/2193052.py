import string

sentence = input("Geef een zin in: ")

newSentence = ""

for letter in sentence:
    if letter not in string.punctuation and letter not in string.digits:
        newSentence += letter
    else:
        newSentence += " "

words = newSentence.split()

for i in range(len(words)):
    print(words[i], len(words[i]))
