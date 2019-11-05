string = input("Give a sentence: ")
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ 0123456789"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
word = ""
i = 0

for letter in string:
    i = i + 1
    if letter in alphabet:
        word = word + letter
    elif letter in punctuation:
        if string[i - 2] in punctuation:
            continue
        else:
            length = len(word)
            print(word, length)
            word = ""
length = len(word)
print(word, length)