def count_words(string):
    space = " "
    count = 0
    for i in range(len(string)):
        if string[i] == space:
            count += 1
    return count