def split(string):
    listy = []
    k = 0
    wordy = ""
    for i in string+" ":
        if i == " ":
            listy.append(wordy)
            k += 1
            wordy = ""
        else:
            wordy += i
    return listy

def remove_punctuation(string):
    punct = '''0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    stringy = ""
    for i in string+" ":
        if i in punct:
            stringy += " "
        else:
            stringy += i
    return stringy

def count_words(string):
    stringy = remove_punctuation(string)
    listy = split(stringy)
    counter = 0
    for i in listy:
        if i != "":
            counter += 1
        else:
            continue
    return counter