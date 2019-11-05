def convert_to_uppercase(s):
    distance = ord('A') - ord('a')
    
    for x in range(len(s)):
        s = s[:x] + chr(ord(s[x])+distance) + s[x+1:]
    
    return s