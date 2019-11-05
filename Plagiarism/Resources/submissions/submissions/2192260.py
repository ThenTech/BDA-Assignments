brol = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
def cleanup(string):
    zonder_brol = ""
    for letter in string:
        if letter not in brol:
            zonder_brol += letter

    return zonder_brol
def count_words(string):
    string = cleanup(string)
    woorden = string.split()
    aantal = len(woorden)
    return aantal
