def findLetter (s, l):
    teller = 0
    while teller < len(s):
        if s[teller] == l:
            return teller
        teller += 1
    return teller

def removeCapitalAndPunctuationAndSpaces (string):
    punctuation = "!\“"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    spatie = " "
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    capitalAlfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fixed = ''

    for i in string:
        if i in punctuation or i in spatie:
            fixed = fixed
        elif i in capitalAlfabet:
            positie = findLetter(capitalAlfabet, i)
            fixed += alfabet[positie]
        else:
            fixed += i
    return fixed


def is_palindrome_sentence(sentence):
    fixedSentence = removeCapitalAndPunctuationAndSpaces(sentence)
    tellerBegin = 0
    tellerEinde = len(fixedSentence) -1

    while tellerBegin < len(fixedSentence):
        if fixedSentence[tellerBegin] == fixedSentence[tellerEinde]:
            tellerBegin += 1
            tellerEinde -= 1
        else:
            return False
    return True