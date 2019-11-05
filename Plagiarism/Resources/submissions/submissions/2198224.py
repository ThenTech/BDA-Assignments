def cleanup_spaces(s):
    spaces = " "
    remove_spaces = ""
    for letter in s:
        if letter not in spaces:
            remove_spaces = remove_spaces + letter + " "
    return remove_spaces