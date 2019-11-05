alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def count_words(string):
    count = 0
    x = 1
    while x <= (len(string) - 2):
        while string[x] in alfabet:
            x += 1
        if string[x] not in alfabet:
            x += 1
        count += 1
    return count
count_words('lol!bbann87ler')
