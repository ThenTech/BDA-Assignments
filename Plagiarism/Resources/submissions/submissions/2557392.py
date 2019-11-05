string = input("Geef een string: ")
alfabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alfabet)):
    count = 0
    for j in range(len(string)):
        if alfabet[i] == string[j]:
            count += 1
    print(alfabet[i], count, sep=": ")