def convert(number):
    whole_cipher = 0
    if number == "":
        return whole_cipher
    whole_cipher += int(number[0]) * (10 ** len(number)-1) + convert(number[1:])
    