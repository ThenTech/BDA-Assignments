def create_sequence(s, index, length):
    count = 0
    bool = True
    hulp = ""

    while bool:
        if index < 0:
            if len(s) + index < 0:
                index = index + len(s)
                bool = True
            else:
                count = index
                bool = False
        else:
            if index > len(s):
                index = index - len(s)
                bool = True
            else:
                count = index
                bool = False

    for i in range(length):
        if count < len(s):
            hulp += s[count]
            count += 1
        else:
            count = 0
            hulp += s[count]
            count += 1
    return hulp
