def count_words(str):
    newString = ""

    for letter in str:
        if letter not in string.punctuation and letter not in string.digits:
            newString += letter
        else:
            newString += " "

    words = newString.split()
    return len(words)