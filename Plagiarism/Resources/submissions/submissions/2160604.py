def create_sequence(string, index, length):
    inf_string = ""
    while len(inf_string) != length:
        string_index = index
        while string_index < 0 or string_index > len(string)-1:
            if string_index < 0:
                string_index += len(string)
            else:
                string_index -= len(string)
        inf_string += string[string_index]
        index += 1
    return inf_string