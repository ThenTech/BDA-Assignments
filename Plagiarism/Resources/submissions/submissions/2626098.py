def create_sequence(string, index, length):
    x = len(string) % index
    string = string[x:x+length]
    length -= len(string)
    if length > 0:
        while True:
            string += string[:length]
            length -= len(string)
            if length ==0:
                return False
    return string