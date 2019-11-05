def create_sequence(string, index, length):
    inf_string = ""
    while len(inf_string) != length:
        string_index = index

        if string_index >= 0 and string_index < 4:
            inf_string += string(string_index)
        elif index < 0:
            string_index -= len(string)
        else:
            string_index += len(string)
        index += 1
    return inf_string