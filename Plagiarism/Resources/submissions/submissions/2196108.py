def check_word(string):
    x = len(string)
    return x

def check_sentence(string):
    word = ""
    for i in string:
        if i in """?;;.:"/,()àç!'""":
            pass
        else:
            word += i
    words = word.split()
    for i in words:
        j = check_word(i)
        print(i, j)