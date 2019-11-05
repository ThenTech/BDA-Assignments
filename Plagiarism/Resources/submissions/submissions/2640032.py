def encode(s, n):
    new_s = ""
    for i in range(len(s)):
        if "a" <= s[i] <= "z":
            if ord(s[i] + n % 26) <= ord("z"):
                new_s += chr(ord(s[i] + n % 26))
            else:
                new_s += chr(ord(s[i] + n % 26) - 26)
        else:
            new_s += s[i]
    return new_s
             
                
def decode(s, n):
    decode_string = encod(s, -n)
    return decode_string