def encode(s, n):
    newstring = ""
    for i in range(len(s)):
        if s[i] in string.ascii_letters:
            number = ord(s[i])
            if 97 <= number <= 122:
                number -= 97
                number = (number + n) % 26
                number += 97
            elif 65 <= number <= 90:
                number -= 65
                number = (number + n) % 26
                number += 65
            letter = chr(number)
            newstring += letter
        else:
            newstring += s[i]
    return newstring


def decode(s, n):
    newstring = ""
    for i in range(len(s)):
        if s[i] in string.ascii_letters:
            number = ord(s[i])
            if 97 <= number <= 122:
                number -= 97
                number = (number - n) % 26
                number += 97
            elif 65 <= number <= 90:
                number -= 65
                number = (number - n) % 26
                number += 65
            letter = chr(number)
            newstring += letter
        else:
            newstring += s[i]
    return newstring