def substring(s, x, y):
    new_str = ""
    for i in range(x, y + 1):
        new_str += s[i]
    return new_str


def find_pos(word, s):
    counter = 0
    while counter < len(s):
        if s[counter] == word[0]:
            ss = substring(s, counter, counter + len(word) - 1)
            if ss == word:
                return counter
        counter += 1
    return None


def in_string(word, s):
    if find_pos(word, s) is not None:
        return True
    return False