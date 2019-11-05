lowercase = 'abcdefghijklmnopqrstuvwxyz'

def cleanup_spaces(s):
    letter = ''
    for i in s:
        if i not in lowercase:
            letter += i
        else: 
            letter += chr(ord(i)-32)
    return letter