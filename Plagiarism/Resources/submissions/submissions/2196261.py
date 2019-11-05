def check_word(string):
    x = len(string)
    return x

def check_sentence(string):
    word = ""
    for i in string:
        if i in """?;;.:"/,()àç!'1234567890""":
            word += ""
        else:
            word += i
    words = word.split()
    for i in words:
        j = check_word(i)
        print(i, j)

check_sentence("one two")
check_sentence("Python! programming     ....  ROCKS")
check_sentence("five 6 seven,eight!nine")
check_sentence("")
check_sentence("This is a simple sentence... cool, right?")