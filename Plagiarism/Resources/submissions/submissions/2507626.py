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

def calc(n,c):
    if n == 0:
        return '  '
    elif n == 1:
        return ' X'
    elif n == 2:
        if c == True:
            return ' X'
        else:
            return 'X '
    else:
        return 'XX'

def decode(s, n=0):

    new_s = ''
    new_s2 = ''

    if len(s) == 1:
        new_s += 'X'
        new_s2 += ' '
    else:
        for i in range(len(s)):
            if i == 0:
                n = int(s[i+1])
                new_s += calc(n,False)[0]
                new_s2 += calc(n,False)[1]
            else:
                if i == len(s)-1:
                    n = int(s[i-1])
                    new_s += calc(n,False)[0]
                    new_s2 += calc(n,False)[1]
                else:
                    n = int(s[i-1]) + int(s[i+1])
                    if n == 2:
                        if len(s)-3 >= i >= 3:
                            x = int(s[i-2]) + int(s[i-1]) + int(s[i+1]) + int(s[i+2])
                            if int(s[i-2]) + int(s[i-1]) + int(s[i+1]) + int(s[i+2]) == 6:
                                new_s += calc(n,True)[0]
                                new_s2 += calc(n,True)[1]
                            else:
                                new_s += calc(n,False)[0]
                                new_s2 += calc(n,False)[1]
                        else:
                            new_s += calc(n,False)[0]
                            new_s2 += calc(n,False)[1]
                    else:
                        new_s += calc(n,False)[0]
                        new_s2 += calc(n,False)[1]
    if new_s == new_s2:
        print(new_s)
    else:
        print(new_s)
        print(new_s2)