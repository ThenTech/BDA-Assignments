def is_letter(char):
    return ("A" <= char and char <= "Z") or \
           ("a" <= char and char <= "z")

def print_words(sentence):
    i = 0

    while(i < len(sentence) and not is_letter(sentence[i])):
        i += 1

    while(i < len(sentence)):
        start_of_word = i

        while(i < len(sentence) and is_letter(sentence[i])):
            i += 1

        word_print = sentence[start_of_word : i]
        print(word_print, len(word_print))

        while(i < len(sentence) and not is_letter(sentence[i])):
            i += 1

def main():
    string = input("Give a sentence: ")

    print_words(string)

main()