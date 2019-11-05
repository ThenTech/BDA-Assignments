import string


def is_palindrome_sentence(sentence):
    new_string = ""
    reverse_string = ""
    for char in sentence:
        if char not in string.punctuation:
            new_string += char
    new_string = new_string.lower().replace(" ", "")
    for i in range(len(new_string)):
        reverse_string += new_string[len(new_string) - 1 - i]
    if new_string == reverse_string:
        return True
    return False