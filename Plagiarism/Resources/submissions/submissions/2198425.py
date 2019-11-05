def encode(s, n):
    n = n%26
    ns = ''
    for x in range(len(s)):
        if s[x] >= 'a' and s[x] <= 'z':
            char = ord(s[x])
            if char > ord('z') - n:
                char -= 26

            if char < ord('a') - n:
                char += 26

            ns += chr(char + n)
        else: ns+=s[x]
    return ns


def decode(s, n):
    n = n%26
    ns = ''
    for x in range(len(s)):
        if s[x] >= 'a' and s[x] <= 'z':
            char = ord(s[x])
            if char > ord('z') + n:
                char -= 26

            if char < ord('a') + n:
                char += 26

            ns += chr(char - n)
        else: ns+=s[x]
    return ns