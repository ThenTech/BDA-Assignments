alphabet = "abcdefghijklmnopqrstuvwxyz"
word = input("Enter your word: \n")
sum = 0

for i in range(len(alphabet)):
    for j in range(len(word)):
        if word[j] == alphabet[i]:
            sum += 1
    print(alphabet[i] + ": " + str(sum))
    sum = 0
