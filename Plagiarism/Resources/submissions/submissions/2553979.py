def filter(string):
    gefilterde_string = ""
    for ch in range(len(string)):
        if 97 <= ord(string[ch]) <= 122:
            gefilterde_string = gefilterde_string + string[ch]
    return gefilterde_string

def teller(string):
    alphabet = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ch in range(len(string)):
        getal = ord(string[ch])
        getal -= 97
        alphabet[getal] += 1
    return alphabet

def uitvoeren(string1, string2):
    filter1 = filter(string1)
    filter2 = filter(string2)
    
    geteld1 = teller(filter1)
    geteld2 = teller(filter2)
    
    if geteld1 == geteld2:
        print(string1, "and", string2, "are anagrams")
    else:
        print(string1, "and", string2, "are not anagrams") 
        
string1 = input("String 1: ")
string2 = input("String 2: ")

uitvoeren(string1, string2)