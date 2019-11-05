word = input("Give me a word: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    count = 0
    for j in range(len(word)):
        if word[j] == i:
            count += 1
    print("Aantal keer ", i, ": ", count, sep="")