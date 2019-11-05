def is_palindrome_sentence(sentence):
    split_sentence = ""
    for i in sentence:
        if i not in " !,:;?.=+()@/0123456789":
            split_sentence += i

    lower_sentence = ""
    for i in split_sentence:
        if i >= "A" and i <= "Z":
            lower_sentence += chr(ord(i) + 32)
        else:
            lower_sentence += i

    reverse = ""

    for i in range(len(lower_sentence)):
        reverse += lower_sentence[len(lower_sentence) - 1 - i]

    if reverse == lower_sentence:
        return True
    else:
        return False
