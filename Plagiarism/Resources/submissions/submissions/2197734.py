def replace(string_1, string_2, string_3):
    length_1 = len(string_1)
    length_2 = len(string_2)
    length_3 = len(string_3)
    for i in range(0, length_3 - length_1 + 2):
        if string_3[i:i + length_1] == string_1:
            string_3 = string_3[:i] + string_2 + string_3[i + length_2 + 1:]
    return(string_3)