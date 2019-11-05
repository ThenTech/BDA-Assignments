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

def calc(n):
    if n == 0:
        return '  '
    elif n == 1:
        return ' X'
    elif n == 2:
        return 'X '
    else:
        return 'XX'

def decode(s, n=0):
    #112121211
    #
    #132424231
    # XXX XXX 
    #XX XXX XX

    #102020201
    #030404030
    # X X X X 

    #0 1 2 3 4
    #    X X X
    #  X   X X

    new_s = ''
    new_s2 = ''

    if len(s) == 1:
        new_s += 'X'
        new_s2 += ' '
    else:
        for i in range(len(s)):
            if i == 0:
                n = int(s[i+1])
                new_s += calc(n)[0]
                new_s2 += calc(n)[1]
            else:
                if i == len(s)-1:
                    n = int(s[i-1])
                    new_s += calc(n)[0]
                    new_s2 += calc(n)[1]
                else:
                    n = int(s[i-1]) + int(s[i+1])
                    new_s += calc(n)[0]
                    new_s2 += calc(n)[1]
    if new_s == new_s2:
        print(new_s)
    else:
        print(new_s)
        print(new_s2)