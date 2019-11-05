def removePunctuation (s):
    punctuation = '''!\"#$%&“”'’()*+,-./:;<=>?@[\\]^_`{|}~'''
    spatie = " "
    fixed = ''

    for i in s:
        if i in punctuation:
            fixed = fixed
        elif i in alfabet or i in spatie:
            fixed += i
    return fixed

alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
string = input("Geef een string: ")
string = removePunctuation(string) + ' '
counter = 0
woord = ''

for i in string:
    if i in alfabet:
        counter += 1
        woord += i
    elif i == ' ' and counter > 0:
        print(woord, counter, sep=" ")
        counter = 0
        woord = ''
