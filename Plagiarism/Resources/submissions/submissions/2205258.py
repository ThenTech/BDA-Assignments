def encode(s, n):
    while n > 26:
        n -= 26
    while n < 0:
        n += 26
    word = ""
    for i in s:
        if i in ",.123456789!;:?[]{})(^ ":
            word += i

        elif ord(i) < 122 - n:
            word += chr(ord(i)+n)
        else:
            k = ord(i) - (26 - n) #122 --> 100, 121 --> 99
            word += chr(k)
    return word