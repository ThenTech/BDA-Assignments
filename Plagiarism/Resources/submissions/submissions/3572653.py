def count_words(string):
    count = 0
    in_word = False
    for i in string:
        if i.isalpha():
            if in_word:
                continue
            else:
                in_word = True
                count += 1
        else:
            in_word = False
    return count