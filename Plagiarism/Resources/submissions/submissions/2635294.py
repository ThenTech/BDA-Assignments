def cleanup_spaces(s):
    new_str=""
    for i in range(s):
        if not(('a'<=i<='z')or('A'<=i<='Z')):
            new_str += i
        else:
            codeA = ord('A')
            value = ord(i)+codeA
            new_str += chr(value)
    return new_str