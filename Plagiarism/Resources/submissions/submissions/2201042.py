def encode(s, n):
    output = ""
    for char in s:
        if char == " ":
            output += char
        elif char.isupper():
            output += chr((ord(char) + n - 65) % 26 + 65)
        else:
            output += chr((ord(char) + n - 97) % 26 + 97)

    return output


def decode(s, n):
    output = ""
    for char in s:
        if char == " ":
            output += char
        elif char.isupper():
            output += chr((ord(char) - n - 65) % 26 + 65)
        else:
            output += chr((ord(char) - n - 97) % 26 + 97)

    return output