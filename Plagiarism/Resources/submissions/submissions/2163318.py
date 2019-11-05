def create_sequence(string, index, length):
    inf_string = ""
    for i in range(length):
        inside_index = index % len(string)
        inf_string += string[inside_index]
        index += 1
    return inf_string