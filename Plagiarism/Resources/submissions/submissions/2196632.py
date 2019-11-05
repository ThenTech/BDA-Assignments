def in_alphabet(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ,.!?"
    for letters in alphabet:
            if letters == letter:
                return True
    return False

def cleanup_spaces(s):
    start = 0
    end = 0
    placeholder = ""
    for i in range(len(s)):
        if in_alphabet(s[i]):
            start = i
            break
    for i in range(len(s)):
        if in_alphabet(s[len(s)-1-i]):
            end = len(s)-1-i
            break
    for i in range(start, end+1):
        placeholder += s[i]
    s = placeholder
    
    counter = 0
    
    if start == 0 and end == 0:
        return ""
    
    while counter < len(s)-1:
        placeholder = ""
        if s[counter] == " " and s[counter+1] == " ":
            place = counter
            for i in range(0, counter+1):
                placeholder += s[i]
            for i in range(counter+2, len(s)):
                placeholder += s[i]
            s = placeholder
            counter = 0
        counter += 1
           
    
    return s
    
