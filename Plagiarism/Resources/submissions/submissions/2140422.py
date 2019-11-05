string = input("Give a word or a sentence: ")
length = len(string)
alphabet = "abcdefghijklmnopqrstuvwxyz"
amount = 0

for letter in alphabet:
    for i in range(length):
        if string[i] == letter:
            amount += 1
    print(letter, ": ", amount, sep="")
    amount = 0
