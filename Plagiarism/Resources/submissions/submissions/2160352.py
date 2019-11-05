def create_sequence(string, index, length):
    string_length = len(string)
    modulo = index % string_length
    final_string = ''
    for i in range(length):
        final_string += string[(modulo+ i) % len(string)]
    return final_string