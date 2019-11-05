def encode(s):
    result = ""
    for i in range(len(s)):
        if len(s) == 1:
            return '0'
        if i == 0:
            if s[i + 1] == 'X':
                result += '1'
            else:
                result += '0'
        elif i == len(s) - 1:
            if s[i - 1] == 'X':
                result += '1'
            else:
                result += '0'
        else:
            temp = 0
            if s[i + 1] == 'X':
                temp += 1
            if s[i - 1] == 'X':
                temp += 1
            result += str(temp)
    return result


def replace(s, value, index):
    if index < (len(s) - 1):
        return s[:index] + value + s[index + 1:]
    else:
        return s[:index] + value


def next(s, x):
    decimal = s+ 1

    binary = '{0:b}'.format(decimal)
    for x in range(len(binary)):
        if binary[x] == '1':
            binary = replace(binary, 'X', x)
        else:
            binary = replace(binary, ' ', x)
    return binary + ' '*(x - len(binary))


def decode(s):
    result = "_" * len(s)
    dumdum = 0
    while not result == "X" * len(s):
        if s == encode(result):
            print(result)
        result = next(dumdum, len(s))
        dumdum+=1
