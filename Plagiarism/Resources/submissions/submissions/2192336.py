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
    while chars < (len(string)-1):
        word_length = 0
        if in_alphabet(string[chars]):
            for characters in range(chars, len(string)):
                if in_alphabet(string[characters]) and characters != len(string)-1:
                    print(string[characters], end="")
                    word_length += 1
                    chars += 1
                if (not in_alphabet(string[characters]))
                    print(" ", word_length, sep="")
                    chars = characters
                    break
                if in_alphabet(string[characters]) and characters == len(string)-1:
                    print(string[characters], end="")
                    word_length += 1
                    chars += 1
                    print(" ", word_length, sep="")
                    chars = characters
                    break
                    
                
        else:
            chars += 1

input = input("string:")
count_words(input)                
        
    