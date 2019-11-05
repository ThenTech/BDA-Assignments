def convert_to_uppercase(s):
    new_str=""
    for i in s:
        if not(('a'<=i<='z')or('A'<=i<='Z')):
            new_str += i
        else:
            codeA = ord('A')
            value = codeA - ord(i)
            new_str += chr(value)
    return new_str