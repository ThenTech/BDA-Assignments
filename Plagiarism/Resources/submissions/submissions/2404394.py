n = 0
whole_cipher = 0
def convert(number):
    global whole_cipher
    if number == "":
        return whole_cipher
    whole_cipher += int(number[n]) * (10 ** len(number))
    convert(number[1:])
    return whole_cipher/10