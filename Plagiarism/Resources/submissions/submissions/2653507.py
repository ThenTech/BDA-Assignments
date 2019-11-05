x = 0
counter = 0

def convert(s):
    global x
    global counter
    if len(s) == 1:
        x = (x * 10) + int(s[0:1])
        return x
    else:
        x = (x * 10) + int(s[0:1])
        counter += 1
        return convert(s[1:])