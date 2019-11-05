def is_letter(ch):
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def each_word(s):
    i = 0

    while i < len(s) and not is_letter(s[i]):
        i += 1

    while i < len(s):
        start_word = i

        while i < len(s) and is_letter(s[i]):
            i += 1

        word = s[start_word:i]
        print(word, len(word))

        while i < len(s) and not is_letter(s[i]):
            i += 1
