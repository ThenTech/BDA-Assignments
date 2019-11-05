def create_sequence(string, index, lenght):
    aantal = (lenght//index)
    if aantal < 0:
        aantal *= -1
    while index < 0:
        index += len(string)
    while index > len(string):
        index -= len(string)
    return string[index:(index+lenght)] * (aantal)
