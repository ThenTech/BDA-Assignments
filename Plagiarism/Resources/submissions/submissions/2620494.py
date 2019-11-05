def to_lowercase(string):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_string = ""
    for i in range(0, len(string)):
        if string[i] in alf:
            new_string += chr(ord(string[i]) + 32)
        else:
            new_string += string[i]
    return new_string

def delete_spaces_and_others(string):
    new_string = ""
    alf = "abcdefghijklmnopqrstuvwxyz"

    for i in string:
        if i in alf:
            new_string += i
    return new_string


def is_palindrome_sentence(string):
    new_string = to_lowercase(string)
    new_string = delete_spaces_and_others(new_string)
    reversed = ""

    for i in range(len(new_string) - 1, -1, - 1):
        reversed += new_string[i]
    for j in range(0, len(new_string)):
        if new_string[j] == reversed[j]:
            continue
        else:
            return False
    return True


