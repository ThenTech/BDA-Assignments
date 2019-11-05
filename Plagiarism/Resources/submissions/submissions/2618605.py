def is_palindrome_sentence(sentence):
    empty_list = []
    for i in sentence:
        empty_list.append(i)

    for i in range(len(empty_list)):
        if 65 <= ord(empty_list[i]) <= 90:
            empty_list[i] = chr(ord(empty_list[i])+32)

    x = ""
    for i in empty_list:
        if 97 <= ord(i) <= 122:
            x += i
    y = ""
    for i in range(len(x)-1,-1, -1):
        y += x[i]

    return x == y