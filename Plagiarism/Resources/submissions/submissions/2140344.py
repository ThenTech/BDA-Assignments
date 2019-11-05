alphabet = "abcdefghijklmnopqrstuvwxyz"
input = input()

for i in range(len(alphabet)):
    som = 0
    print(alphabet[i],": ", sep='', end='')
    for j in range(len(input)):
        if alphabet[i] == input[j]:
            som += 1
    print(som)