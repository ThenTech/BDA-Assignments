def create_sequence(string, index, length):
    a = ""
    ln_string = len(string)
    while index < -ln_string:
        index = index + ln_string
    while index > ln_string:
        index = index - ln_string
    for i in range(length):
        if index < ln_string:
            a = a + string[index]
            index = index + 1
        else:
            index = index - ln_string
            a = a + string[index]
            index = index + 1
    return a