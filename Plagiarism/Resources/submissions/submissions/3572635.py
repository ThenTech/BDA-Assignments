def count_words(string):
    count = 0
    out_word = True
    for i in string:
        if i.isalpha() and !out_word:
            out_word = True
            count += 1
        else:
            out_word = False
    print(count)