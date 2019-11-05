alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encode(s, n):

    x=''
    # a = 97
    # z = 122

    for i in s:
        if i not in alphabet:
            x += i
        else:
            if ord('a') <= ord(i) + (n%26) <= ord('z'):
                x += chr(ord(i)+(n%26))
            elif ord(i) + (n%26) >= ord('z'):
                x += chr(ord(i)+(n%26) - 26)
            elif ord(i) + (n%26) <= ord('a'):
                x += chr(ord(i)+(n%26) + 26)
    
    return x

def decode(s, n):
    x = encode(s,-n)
    return x