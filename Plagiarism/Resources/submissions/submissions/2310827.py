def move_letter(s, n):
s = input("Message: ")
n = int(input("Number: "))
    result = ""

    for ch in s:
        if 'a' <= ch <= 'z':
            number = ord(ch) - ord('a')
            number = (number + n) % 26
            result += chr(number + ord('a'))
        else:
            result += ch
    return result


def encode(s, n):
    return move_letter(s, n)


def decode(s, n):
    return move_letter(s, -n)




