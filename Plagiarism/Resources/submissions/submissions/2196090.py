def check_word(string):
    print(string, len(string))

def check_sentence(string):
    word = ""
    for i in string:
        if i in """?;;.:"/,()àç!'""":
            pass
        else:
            word += i
    words = word.split()
    for i in words:
        check_word(i)