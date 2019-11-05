def cleanup_spaces(s):
    difference = ord('a') - ord('A')
    new_string = ""
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            new_string += chr(ord(i)-difference)
        else:
            new_string += i
    return new_string