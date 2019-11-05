string = str(input())


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
    clean_word = print_word(word)
    if len(clean_word) == 0:
        continue
    else:
        print((clean_word), len(clean_word))
