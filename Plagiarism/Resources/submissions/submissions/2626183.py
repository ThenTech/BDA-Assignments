def create_sequence(string, index, length):
    x = index%len(string)
    string123 = string[x:x+length]
    length -= len(string)
    if length > 0:
        while True:
            string123 += string[:length]
            length -= len(string)
            if length ==0:
                return False
    return string123