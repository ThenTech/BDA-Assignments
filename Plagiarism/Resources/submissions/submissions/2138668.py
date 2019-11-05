word = input('Word?')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
i = len(word) - 1
q = 0

for k in range(len(alphabet)):
    while i >= 0:
        if word[i] == alphabet[k]:
            q += 1
        i -= 1
    print(alphabet[k], ':', ' ', q, sep='')
    i = len(word) - 1
    q = 0