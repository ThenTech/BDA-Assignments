alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def encode(s, n):

    x=''

    for i in s:
        if i not in alphabet:
            x += i
        else:
            if ord(i)+n < ord('a'):
                x += chr(ord(i)+ n + 26)
            elif ord(i)+n > ord('z'):
                x += chr(ord(i)+ n - 122 +96)
            else:
                x += chr(ord(i)+n)
    return x

def decode(s, n):
    x = encode(s,-n)
    return x