def create_sequence(string, index, length):
    str_len = len(string)
    first_char = index % str_len
    
    for x in range(length):
        curr_chr = (first_char + x) % str_len
        print(string[curr_chr], end="")
    print()