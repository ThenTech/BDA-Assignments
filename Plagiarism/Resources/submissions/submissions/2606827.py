def create_sequence(string, index, length):
    smaller_index_str = string[index:]
    new_string = smaller_index_str + string
    len_new_str = len(new_string)
    while len_new_str < length:
        for i in string:
            if len(new_string) < length:
                new_string += i
        len_new_str = len(new_string)
    return new_string