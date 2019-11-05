def is_letter(ch):
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def each_word(string):
    i = 0

    while i < len(string) and not is_letter(string[i]):
        i += 1

    while i < len(string):
        start_word = i

        while i < len(string) and is_letter(string[i]):
            i += 1

        word = string[start_word:i]
        print(word, len(word))

        while i < len(string) and not is_letter(string[i]):
            i += 1

each_word(string)
print()