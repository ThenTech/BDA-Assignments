string = input("Give a sentence: ")
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ 0123456789"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
word = ""
i = 0

if string not in "":
    for letter in string:
        i = i + 1
        if letter in alphabet:
            if i == len(string):
                word = word + letter
                length = len(word)
                print(word, length)
            else:
                word = word + letter
        elif letter in punctuation:
            if string[i - 2] in punctuation:
                word = ""
                length = ""
                continue
            else:
                length = len(word)
                print(word, length)
                word = ""