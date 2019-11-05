n = 0
def convert(number):
    whole_cipher = 0
    if number == "":
        return whole_cipher
    whole_cipher += int(number[n]) * (10 ** len(number)) + convert(number[1:])
    return whole_cipher