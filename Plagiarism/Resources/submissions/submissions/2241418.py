def convert_to_uppercase(s):
    for x in s:
        if 'a' <= x <= 'z':
            y = chr(ord(x) - ord('a') + ord('A'))
            print(y, end="")
        else:
            print(x, end="")