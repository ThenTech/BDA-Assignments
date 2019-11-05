def is_letter(ch):
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def print_word(word):
    clean_word = ""
    for ch in word:
        if is_letter(ch):
            clean_word += ch
    return clean_word


string_list = string.split()

for word in string_list:
    if len(print_word(word)) == 0:
        pass
    else:
        print(print_word(word), len(print_word(word)))