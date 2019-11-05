woord = input("Geef een woord op: ")
alfabet = "abcdefghijklmnopqrstuvwxyz"

for char in alfabet:
    count = 0
    for j in range(len(woord)):
        if(char == woord[j]):
            count += 1
    print(char, count, sep=": ")