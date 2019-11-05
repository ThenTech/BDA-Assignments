def encode(s):
    result = ""
    for i in range(len(s)):
        if len(s) == 1:
            return '0'
        if i == 0:
            if s[i+1] == 'X':
                result += '1'
            else:
                result += '0'
        elif i==len(s)-1:
            if s[i-1] == 'X':
                result += '1'
            else:
                result += '0'
        else:
            temp = 0
            if s[i+1] == 'X':
                temp+=1
            if s[i-1] == 'X':
                temp+=1
            result+=str(temp)
    return result


def decode(s):
    pass