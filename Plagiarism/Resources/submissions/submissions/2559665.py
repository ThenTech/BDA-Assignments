def encode(s, n):
    encoded=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        if s[i] in alphabet:
            for j in range(len(alphabet)):
                if s[i]==alphabet[j]:
                    if j+n<26:
                        encoded+=alphabet[j+n]
                    elif n==26:
                            encoded += alphabet[j + (n-26)]
                    elif n>26:
                        if j+(n-26)<26:
                            encoded+= alphabet[j + (n-26)]
                        elif j+(n-26)==26:
                            encoded+=alphabet[0]
                        elif j==25:
                            encoded+=alphabet[n-26-1]
                        elif j+(n-26)>26:
                            encoded+= alphabet[j+(26-n)]




        else:
            encoded+=s[i]

    return encoded

def decode(s, n):
    decoded=""
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(s)):
        if s[i] in alphabet:
            for j in range(len(alphabet)):
                if s[i]==alphabet[j]:
                    if n>0 and n<26:
                        decoded+=alphabet[j-n]
                    elif n>26:
                        decoded += alphabet[j-n+26]
                    elif n<0:
                        decoded += alphabet[j-n - 26]
        else:
            decoded+=s[i]

    return decoded
