def encode(s, n):
    new_string = ''
    for i in s:
        if ord('a') <= ord(i) < ord('z')-n:
            new_string += chr(ord(i)+n)
        elif ord('z')- n < ord(i) <= ord('z'):
            new_string += chr(ord(i)+n-26)
        else:
            new_string += i
    return new_string


def decode(s, n):
    new_string = ''
    for i in s:
        if ord('a') <= ord(i) < ord('a')+n:
            new_string += chr(ord(i) - n + 26)
        elif ord('a')+n <= ord(i) <= ord('z'):
            new_string += chr(ord(i)-n)
        else:
            new_string += i
    return new_string