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

woorden = remove_punctuation(zin).split()

for x in range(len(woorden)-2):
    for element in woorden:
        for letter in element:
            if letter in alfabet:
                woord += letter
            else:
                continue


        print(woord, len(woord))
        woord = ''