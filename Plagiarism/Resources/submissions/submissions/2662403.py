# write your code here
def find_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word = ""
    in_word = False
    
    for char in string:
        if char in alphabet and in_word == False:
            in_word = True
            word += char
        
        elif char in alphabet and in_word == True: 
            word += char
            
        elif char not in alphabet or char == string[len(string)-1] and in_word == True:
            in_word = False
            print(word, len(word))
            word = ""
            
string = input()
find_words(string)