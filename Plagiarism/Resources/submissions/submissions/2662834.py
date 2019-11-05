def is_palindrome_sentence(sentence):
    sentence = make_up(sentence)
    
    for char in range(len(sentence)//2):
        if not sentence[char] == sentence[len(sentence)-char-1]:
            return False
    
    return True
    
    
    
def make_up(sentence):
    returnsentence = ''
    for char in sentence:
        if obj('a') <= obj(char) <= obj('z'):
            returnsentence += char
        
        if obj('A') <= obj(char) <= obj('Z'):
            returnsentence += chr(obj(char) + (obj('a') - obj('A')))
    
    return returnsentence