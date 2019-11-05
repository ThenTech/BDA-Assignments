sentence = input("Give a sentence: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == char:
            count += 1
    print(char, ": ", count, sep="")
