def encode(input_string):
    encoded_str = ""

    for index in range(len(input_string)):
        line_count = 0
        if index == 0 and len(input_string) > 1:
            if input_string[index + 1] == "X":
                line_count += 1
        elif index == len(input_string) - 1 and len(input_string) > 1:
            if input_string[index - 1] == "X":
                line_count += 1
        elif len(input_string) > 2:
            if input_string[index - 1] == "X":
                line_count += 1
            if input_string[index + 1] == "X":
                line_count += 1

        encoded_str += str(line_count)

    return encoded_str

def decode():
    pass