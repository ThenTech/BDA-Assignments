def is_palindrome_sentence(sentence):
    sentence = make_up(sentence)
    
    for char in range(len(sentence)//2):
        if not sentence[char] == sentence[len(sentence)-char-1]:
            return False
    
    return True
    
    
    
def make_up(sentence):
    returnsentence = ''
    for char in sentence:
        if ord('a') <= ord(char) <= ord('z'):
            returnsentence += char
        
        if ord('A') <= ord(char) <= ord('Z'):
            returnsentence += chr(ord(char) + (ord('a') - ord('A')))
    
    return returnsentence