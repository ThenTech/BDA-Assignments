def substring(str, start, lenght):
    new_str = ""
    if start+lenght > len(str):
        return
    for i in range(start+lenght):
        if i >= start:
            new_str += str[i]
    return new_str

def find_pos(word, stringy):
    counter = 0
    for i in stringy:
        if word[0] == i:
            if substring(stringy, counter, len(word)) == word:
                return counter
            counter += 1
        else:
            counter += 1

def in_string(word, stringy):
    if find_pos(word, stringy) == None:
        return False
    else:
        return True