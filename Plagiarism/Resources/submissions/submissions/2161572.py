def create_sequence(string, index, length):
    woord = ""
    c = 0
    lang = str((length + 1) * string * index)
    while index < 0:
        index = len(string)+index
    while c < length:
        k = lang[index+c]
        woord += k
        c += 1
    return woord