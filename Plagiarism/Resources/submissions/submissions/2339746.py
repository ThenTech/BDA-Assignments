def rotate(s):
    result = ""
    for ch in s:
        if ('a' <= ch and ch <= 'z'):
            number = ord(ch) - ord('a')
            number = (number) % 26
            result += chr(number + ord('a'))
        else:
            result += ch
    return result





s = input("Message: ")
print(rotate("abc"))
