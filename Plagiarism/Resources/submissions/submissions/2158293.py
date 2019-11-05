def print_relativechar(string, i):
    length_string = len(string)
    
    if i >= len(string):
        while i >= len(string):
            i = i - len(string)
        
    print(string[i], end="")


def create_sequence(string, index, length):
    if index < 0:
        index = 1 + index
        
    for i in range(index, index+length):
        print_relativechar(string, i)
    print()