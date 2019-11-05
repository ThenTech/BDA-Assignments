def encode(s, n):
    new = ""
    for i in range(len(s)):
        new += chr(((ord(s[i]) - ord('a') + n) % 26) + ord('a'))
    return new


def decode(s, n):
    new = ""
    for i in range(len(s)):
        new += chr(((ord(s[i]) - ord('a') - n) % 26) + ord('a'))
    return new
