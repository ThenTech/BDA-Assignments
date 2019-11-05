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
    punct = ''' "`~!@1234567890#$%^.&:*()_+.=-;[]{}\|/?><., '''
    stringy = ""
    for i in string+" ":
        if i in punct:
            stringy += " "
        else:
            stringy += i
    return stringy

def new_listy(string):
    stringy = remove_punctuation(string)
    listy = split(stringy)
    listy2 = []
    counter = 0
    for i in listy:
        if i != "":
            listy2.append(i)
        else:
            listy2
    return listy2

def is_palindrome_sentence(sentence):
    listy = new_listy(sentence)
    for i in listy:
        counter = 0
        for j in i:
            counter += 1
        print(i, counter)
    return