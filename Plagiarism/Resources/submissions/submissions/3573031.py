def encode(s):
    output = []
    for i in range(0, len(s)):
        counter = 0
        if i - 1 >= 0:
            if s[i - 1] == 'X':
                counter += 1
        if i + 1 < len(s):
            if s[i + 1] == 'X':
                counter += 1
        output.append(counter)

    string = ""
    for i in output:
        string += str(i)
    return string

def decode(s):
    pass