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

def replace(s, value, index):
    if index < len(s)-1:
        return s[:index] + value + s[index+1:]
    else:
        return s[:index] + value

def decode(s):
    result="_"*len(s)
    for x in range(len(s)):
        if s[x] == '2':
            result = replace(result, x-1, 'X')
            result = replace(result, x+1, 'X')
        elif s[x] == '0':
            result = replace(result, x-1, ' ')
            result = replace(result, x+1, ' ')
    
    for x in range(len(s)):
        canLeft = True
        lastLeft = 0
        if s[x] == '1':
            if x == 0:
                result = replace(result, x+1, ' ')
                canLeft = false
            if x-lastleft == 2 and canLeft:
                result = replace(result, x-1, 'X')
                canLeft = True
            elif x-lastleft == 2 and not canLeft:
                result = replace(result, x+1, 'X')
                canLeft = False
            elif x-lastleft < 2:
                result = replace(result, x+1, 'X')
            elif x-lastleft > 2:
                result = replace(result, x+1, 'X')
                canLeft = True
    print( result )