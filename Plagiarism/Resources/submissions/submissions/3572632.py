def count_words(string):
    count = 0
    out_word = True
    for i in string:
        if (i < 'a' or i > 'z') and !out_word:
            if i < 'A' or i > 'Z':
                out_word = True
                count += 1
        else:
            out_word = False
    print(count)