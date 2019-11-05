alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
woord = input("woord: ")
for x in range(len(woord)):
    if woord[x] in alfabet:
        print(woord, len(woord))