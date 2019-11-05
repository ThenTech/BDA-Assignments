def is_letter(char):
    return ("A" <= char and char <= "Z") or \
           ("a" <= char and char <= "z")

def count_words(string):
    """
        Count ``words'' (alphabet-sequences).
    """
    words = 0
    i = 0

    # skip initial non-words
    while (i < len(string) and not(is_letter(string[i]))):
        i += 1

    # read words, followed by non-words
    while (i < len(string)):
        words += 1

        # skip the word
        while (i < len(string) and is_letter(string[i])):
            i += 1

        # skip the non-word after the word
        while (i < len(string) and not(is_letter(string[i]))):
            i += 1

    return words



for string in ["one", "one two", \
               "test3four", "five 6 seven,eight!nine"]:
    print(count_words(string))