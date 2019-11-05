def cleanup_spaces(s):
    distance = ord('A') - ord('a')
    
    for x in range(len(s)):
        s[x] = chr(ord(s[x])+distance)
    
    return s