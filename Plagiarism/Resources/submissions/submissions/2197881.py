def encode(s, n):
    ns = ''
    for x in range(len(s)):
        if s[x] >= 'a' and s[x] <= 'z':
            char = ord(s[x])
            if char > ord('z') - n:
                char -= 26

            ns += chr(char + n)
    return ns


def decode(s, n):
    ns = ''
    for x in range(len(s)):
        if s[x] >= 'a' and s[x] <= 'z':
            char = ord(s[x])
            if char < ord('a') + n:
                char += 26

            ns += chr(char - n)
    return ns