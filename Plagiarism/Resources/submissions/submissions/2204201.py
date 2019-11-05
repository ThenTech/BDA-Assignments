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

def next(s):
    length = len(s)
    binary = ''
    for x in s:
        if x == 'X':
            binary += 1
        else:
            binary += 0
    
    decimal = int(binary, 2)
    decimal += 1
    
    binary = '{0:b}'.format(decimal)
    for x in s:
        if x=='1':
            s = replace(s,'X', x)
        else:
            s = replace(s,' ', x)
    return s+' '*(length-len(s))
    
    

def decode(s):
    result="_"*len(s)
    while result == "X"*len(s):
        if s == encode(result):
            print(result)
        result = next(result)