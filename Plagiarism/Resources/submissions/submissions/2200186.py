lowercase = 'abcdefghijklmnopqrstuvwxyz'

def convert_to_uppercase(s):
    letter = ''
    for i in s:
        if i not in lowercase:
            letter += i
        else: 
            letter += chr(ord(i)-32)
    return letter