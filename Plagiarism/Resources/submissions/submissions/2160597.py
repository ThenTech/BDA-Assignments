def create_sequence(string, index, length):
    inf_string = ""
    while len(inf_string) != length:
        print("LENGTH:", len(inf_string))
        string_index = index
        print("1:", string_index)
        while string_index < 0 or string_index > len(string)-1:
            if string_index < 0:
                string_index += len(string)
            else:
                string_index -= len(string)
        print("2:", string_index)
        inf_string += string[string_index]
        index += 1
    return inf_string