import string

sentence = input(" ")
sentence1 = ""
for letter in sentence:
    if letter in string.ascii_letters or letter == " ":
        sentence1 += letter
    else:
        sentence1 += " "
split = sentence1.split()
for x in split:
    print(x, len(x))