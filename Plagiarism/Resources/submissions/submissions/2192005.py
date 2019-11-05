def count_words(string):
    ab = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    count = 0
    last_letter = False
    for x in string:
        if not last_letter and x in ab:
            last_letter = True
            count += 1
        elif x not in ab:
            last_letter = False
    return count