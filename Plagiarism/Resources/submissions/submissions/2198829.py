punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~“”’"
numbers = "1234567890"
s = input("Sentence: ")
for letter in s:
    if letter in punctuation:
        s = s.replace(letter, " ")
for letter in s:
    if letter in numbers:
        s = s.replace(letter, " ")
ws = s.split()
for i in ws:
    print(i, len(i))
    