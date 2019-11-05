def create_sequence(string, index, length):
    str_len = len(string)
    first_char = index % str_len
    
    new_string = ""
    
    for x in range(length):
        curr_chr = (first_char + x) % str_len
        new_string += string[curr_chr]
    return new_string