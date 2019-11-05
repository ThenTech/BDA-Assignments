def encode(s, n):
    new_string = ""
    for i in s:
        while ord(i) + n < ord('a'):
            n += 26
        while ord(i) + n > ord('z'):
            n -= 26
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            new_string += chr(ord(i)+n)
        else:
            new_string += i
    return new_string

def decode(s, n):
    return encode(s, -n)