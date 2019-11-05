# write your code here
def find_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word = ""
    in_word = False
    
    for i in range(len(string)):
        char = string[i]
        if char in alphabet and in_word == False:
            in_word = True

        if char in alphabet and in_word == True: 
            word += char
        
        elif char not in alphabet and in_word == True:
            in_word = False
            print(word, len(word))
            word = ""
            
        if char in alphabet and in_word == True and i == len(string)-1:
            print(word, len(word))
            
string = input()
find_words(string)