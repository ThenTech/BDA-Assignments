import string


def count_words(s):
    new_string = ""
    count = 0
    for char in s:
        if char not in string.punctuation:
            new_string += char
        else: new_string += " "
    sl = new_string.split(" ")
    for i in sl:
        test = True
        for j in i:
            if j not in string.ascii_letters:
                test = False
                break
        if test:
            count += 1
    print(count)