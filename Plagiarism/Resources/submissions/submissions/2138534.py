word = input('Word?')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
i = len(word) - 1
q = 0

for k in range(len(alphabet)-1):
    while i >= 0:
        if word[i] == alphabet[k]:
            q += 1
        i -= 1
    print(alphabet[k], ':', q)
    i = len(word) - 1
    q = 0
