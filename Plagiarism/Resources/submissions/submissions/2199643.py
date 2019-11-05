punctuation = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~0123456789 "

def count_words(string):
    total = 0
    if string == "":
        return 0
    if len(string) < 2:
        return 0
    for i in range(0, len(string) - 1):
        letter = string[i]
        next_letter = string[i+1]
        if letter in punctuation:
            if next_letter in punctuation:
                total = total
            else:
                total = total + 1
        else:
            continue
    return total + 1

    if string == "":
        return 0
    if len(string) < 2:
        return 0
    for i in range(0, len(string) - 1):
        letter = string[i]
        next_letter = string[i+1]
        if letter in punctuation:
            if next_letter in punctuation:
                total = total
            else:
                total = total + 1
        else:
            continue
    return total + 1
