zin = input("Geef hier je zin in")
alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

woord = ''

import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
        else:
            s_without_punct += ' '
    return s_without_punct

woorden = remove_punctuation(zin).split()

for element in woorden:
    for letter in element:
        if letter in alfabet:
            woord += letter
        else:
            break
    if len(woord) == 0:
        continue
    if len(woord) != 0:
        print(woord, len(woord))
    woord = ''