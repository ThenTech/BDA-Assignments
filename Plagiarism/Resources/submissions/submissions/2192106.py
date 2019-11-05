alphabet = "abcdefghijklmnopqrstuvwxyz"


def reverse_string(string):
    output = ""
    for i in range(len(string)):
        output += string[len(string)-i-1]
    return output


def remove_layout(sentence):
    sentence = sentence.lower()
    output = ""
    for i in sentence:
        if i in alphabet:
            output += i
        else:
            output += ""
    return output


def is_palindrome_sentence(sentence):
    original = remove_layout(sentence)
    palindrome = reverse_string(original)

    return original == palindrome
