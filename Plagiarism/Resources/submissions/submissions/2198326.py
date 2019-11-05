def encode(s, n):
    encoded_word = ""
    for chars in s:
        new_char = chars
        if 97 <= ord(chars) and ord(chars) <= 122:
            if n >= 0:
                n = n % 26
                new_char_int = (ord(chars) + n)
            if n < 0:
                n = n % 26
                new_char_int = (ord(chars) + (26+n))
                
            if new_char_int > 122:
                new_char = chr(97 + (new_char_int) - 123)
            else:
                new_char = chr(new_char_int)
        encoded_word += new_char
    return encoded_word
        


def decode(s, n):
    return encode(s, -n)