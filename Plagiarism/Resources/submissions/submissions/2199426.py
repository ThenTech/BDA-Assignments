def encode(s):
    q = 0
    new_string = ''
    for i in range(len(s)):
        if i < len(s)-1 and s[i+1] == 'X':
            q += 1
        if i > 0 and s[i-1] == 'X':
            q += 1
        new_string += str(q)
        q = 0
    return new_string


def decode(s, n):
    pass