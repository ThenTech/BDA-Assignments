def is_palindrome_sentence(sentence):
    sentence_list = []
    for i in sentence:
        if i > 'a' and i < 'z':
            sentence_list.append(i)
        if i > 'A' and i < 'Z':
            letter = ord(i)
            letter -= ord('A')
            letter += ord('a')
            sentence_list.append(chr(letter))
    string = ""
    for i in sentence_list:
        string += i
    sentence_list.reverse()
    rev_string = ""
    for i in sentence_list:
        rev_string += i
    if string == rev_string:
        return True
    return False