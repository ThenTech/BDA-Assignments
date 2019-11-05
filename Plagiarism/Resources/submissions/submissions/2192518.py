def is_palindrome_sentence(sentence):
    alfabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    enkelletters = ''
    for letter in sentence:
        if letter in alfabet:
            enkelletters += letter
    enkelkleineletters = enkelletters.lower()
    aantalletters = len(enkelkleineletters)
    for letter in enkelkleineletters:
        if letter == enkelkleineletters[aantalletters-1]:
            aantalletters -= 1
        else:
            return False
    return True

is_palindrome_sentence("stevevets")