alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def count_words(string):
    count = 0
    x = 0
    while x <= len(string): 
        while string[x] in alfabet:
            x += 1
            if x == len(string):
                    break
        if x == len(string):
            break
        while string[x] not in alfabet:
            x += 1
            if x == 0:
                continue
        count += 1
    return count

