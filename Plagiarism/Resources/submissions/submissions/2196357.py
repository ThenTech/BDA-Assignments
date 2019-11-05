def in_alphabet(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ"
    for letters in alphabet:
            if letters == letter:
                return True
    return False

def cleanup_spaces(s):
    placeholder = ""
    for i in range(len(s))
        if in_alphabet(i):
            start = i
            break
    for i in range(len(s)):
        if in_alphabet(len(s)-1-i):
            end = len(s)-1-i
            break
    for i in range(start, end+1):
        placeholder += s[i]
    s = placeholder
    
    counter = 0
    
    while counter < len(s)
        placeholder = ""
        if s[counter] == " " and s[counter+1] == " ":
            place = counter
            for i in range(0, counter+1):
                placeholder += s[i]
            for i in range(counter+2, len(s))
                placeholder += s[i]
            s = placeholder
            counter = 0
            
    return s