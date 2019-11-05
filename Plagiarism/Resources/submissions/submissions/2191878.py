def count_words(string):
    counter = 1
    for i in range(len(string)):
        if string[i] == " ":
            counter += 1
    return counter