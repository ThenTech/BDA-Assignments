zin = input("Geef hier je zin in")
alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
woord = ''


import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

remove_punctuation(zin)
woorden = remove_punctuation(zin).split()

for x in range(len(woorden)-1):
    for woord in woorden:
        for letter in woord:
            if letter in alfabet:
                woord += letter
            else:
                continue


        print(woord, len(woord))
        woord = ''