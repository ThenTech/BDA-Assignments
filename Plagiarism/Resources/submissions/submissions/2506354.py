def encode(s, n=0):
    new_s = ''

    if len(s) == 1:
        new_s += '0'
    else:
        for i in range(len(s)):
            if i == 0:
                if s[i+1] == 'X':
                    new_s += '1'
                else:
                    new_s += '0'
            else:
                if i == len(s)-1:
                    if s[i-1] == 'X':
                        new_s += '1'
                    else:
                        new_s += '0'
                else:
                    if s[i-1] == 'X' and s[i+1] == 'X':
                        new_s += '2'
                    elif s[i-1] == 'X':
                        new_s += '1'
                    elif s[i+1] == 'X':
                        new_s += '1'
                    else:
                        new_s += '0'
    return new_s

def decode(s, n=0):
    pass