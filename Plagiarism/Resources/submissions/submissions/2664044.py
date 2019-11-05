def is_letter(char):
    return ("A" <= char and char <= "Z") or \
           ("a" <= char and char <= "z")

def print_words(string):
    words = 0
    i = 0

    # skip initial non-words
    while (i < len(string) and not(is_letter(string[i]))):
        i += 1

    # read words, followed by non-words
    while (i < len(string)):
        start_of_word = i

        # skip the word
        while (i < len(string) and is_letter(string[i])):
            i += 1

        word = string[start_of_word:i]
        print(word, len(word))


        # skip the non-word after the word
        while (i < len(string) and not(is_letter(string[i]))):
            i += 1



for string in ["one", "one two", \
               "test3four", "five 6 seven,eight!nine"]:
    print_words(string)
    print()