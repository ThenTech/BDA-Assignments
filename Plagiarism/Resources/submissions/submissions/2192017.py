def in_alphabet(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    for letters in alphabet:
            if letters == letter:
                return True
    return False



def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    word_counter = 0
    for characters in range(len(string)-1):
        word_length = 0
        if in_alphabet(string[characters]):
            for chars in range(characters, len(string)-1):
                if in_alphabet(string[chars]):
                    print(string[chars], end="")
                    word_length += 1
                if not in_alphabet(string[chars]):
                    print(" ", word_length, sep="")
                    break

input = input("string:")
count_words(input)                
        
    