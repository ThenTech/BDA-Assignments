def convert(string):
    result = 0
    for i in string:
        result *= 10
        for d in '0123456789':
            result += i > d
    return result
