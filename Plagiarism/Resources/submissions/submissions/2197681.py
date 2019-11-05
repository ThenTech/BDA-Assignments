def encode(s, n):
    new_string = ''
    for i in s:
        if 'A' <= i <= 'Z':
            q = ord(i)- ord('A')+ n
            new_string += chr(q % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            q = ord(i) - ord('a') + n
            new_string += chr(q % 26 + ord('a'))
        else:
            new_string += i
    return new_string


def decode(s, n):
    new_string = ''
    for i in s:
        if 'A' <= i <= 'Z':
            q = ord(i) - ord('A') - n
            new_string += chr(q % 26 + ord('A'))
        elif 'a' <= i <= 'z':
            q = ord(i) - ord('a') - n
            new_string += chr(q % 26 + ord('a'))
        else:
            new_string += i
    return new_string