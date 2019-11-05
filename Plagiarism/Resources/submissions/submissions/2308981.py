def is_letter (char):
    return ("a" <= char <= "z") or ("A" <= char <= "Z")


def print_words(string):
    word = 0
    i = 0

    while (i < len(string)) and not (is_letter(string[i])):
        i += 1

    while i < len(string):
        start_of_word = i

        while (i < len(string)) and (is_letter(string[i])):
            i += 1

        word = string[start_of_word:i]
        print(word, len(word))

        while (i < len(string) and not (is_letter(string[i]))):
            i += 1