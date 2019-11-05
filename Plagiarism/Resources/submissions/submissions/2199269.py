alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def count_words(string):
    count = 0
    x = 0
    if string[x] not in alfabet:
        break
    while x <= len(string): 
        while string[x] in alfabet:
            x += 1
            if x == len(string):
                break
        count += 1
        if x == len(string):
            break
        while string[x] not in alfabet:
            x += 1
            if x == 0:
                continue
    return count

