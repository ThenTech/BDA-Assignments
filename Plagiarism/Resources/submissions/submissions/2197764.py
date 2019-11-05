def encode(s, n):
    encoded_word = ""
    for chars in s:
        new_char = chars
        if 97 <= ord(chars) and ord(chars) <= 122:
            new_char = int(ord(chars) + n)
            if new_char > 122:
                new_char = chr(97 + (int(new_char) - 123))
        encoded_word += new_char
    return encoded_word
        


def decode(s, n):
    pass