def filter(string):
    nieuwe_string =""
    alfabet = "azertyuiopqsdfghjklmwxcvbn"
    for el in string:
        if el.lower() in alfabet:
            nieuwe_string = nieuwe_string + el.lower()
    return nieuwe_string

def is_palindrome_sentence(string):
    bool = True
    for el in range(len(string)//2):
        if string[el] != string[len(string)-1-el]:
            bool = False
        if bool == False:
            return False
    return True
is_palindrome_sentence()