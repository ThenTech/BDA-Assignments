def rotate(s, n):
    result = ""
    for ch in s:
        if ('a' <= ch and ch <= 'z'):
            number = ord(ch) - ord('a')
            number = (number + n) % 26
            result += chr(number + ord('a'))
        else:
            result += ch
    return result


def encode(s, n):
    return rotate(s, n)


def decode(s, n):
    return rotate(s, -n)



s = input("Message: ")
n = int(input("Number: "))
print(encode(s, n))
print(decode(encode(s, n), n))
