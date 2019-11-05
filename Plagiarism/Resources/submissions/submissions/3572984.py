def is_palindrome_sentence(sentence):
    sentence = []
    for i in sentence:
        if i > 'a' and i < 'z':
            sentence.append(i)
        if i > 'A' and i < 'Z':
            letter = ord(i)
            letter -= ord('A')
            letter += ord('a')
            sentence.append(chr(letter))
    string = ""
    for i in sentence:
        string += i
    sentence.reverse()
    rev_string = ""
    for i in sentence:
        rev_string += i
    if string == rev_string:
        return True
    return False