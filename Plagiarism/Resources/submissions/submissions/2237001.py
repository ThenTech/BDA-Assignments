def encode(s, n):
    output = ""
    if n < 0:
        n = 26 + n
    elif n//26 > 0:
        a = n//26
        n = n - a*26
    for i in range(len(s)):
        if s[i] <= chr(64):
            output += s[i]
        elif chr(ord(s[i]) + n) >= chr(91) and chr(ord(s[i]) + n) <= chr(96) or chr(ord(s[i]) + n) >= chr(123) :
            output += chr(ord(s[i]) - 26 + n)
        else:
            output += chr(ord(s[i]) + n)

    return output


def decode(s, n):
    output = ""
    if n < 0:
        n = 26 + n
    elif n // 26 > 0:
        a = n // 26
        n = n - a * 26
    n = 26 - n
    for i in range(len(s)):
        if s[i] <= chr(64):
            output += s[i]
        elif chr(ord(s[i]) + n) >= chr(91) and chr(ord(s[i]) + n) <= chr(96) or chr(ord(s[i]) + n) >= chr(123):
            output += chr(ord(s[i]) - 26 + n)
        else:
            output += chr(ord(s[i]) + n)

    return output

print(decode("hswohila: myvt h av g", 33))