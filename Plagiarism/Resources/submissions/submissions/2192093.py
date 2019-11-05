def in_alphabet(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    for letters in alphabet:
            if letters == letter:
                return True
    return False



def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    word_counter = 0
    chars = 0
    while chars <= (len(string)-1):
        word_length = 0
        endword = False
        if in_alphabet(string[chars]):
            for characters in range(chars, len(string)-1):
                if in_alphabet(string[characters]) and not endword:
                    print(string[chars], end="")
                    word_length += 1
                if not in_alphabet(string[characters]) and not endword:
                    print(" ", word_length, sep="")
                    endword = True
                    chars = characters
        else:
            chars += 1

input = input("string:")
count_words(input)                
        
    