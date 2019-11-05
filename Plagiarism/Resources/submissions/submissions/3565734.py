sentence = input("Give sentence: ")
length = len(sentence)
new_sent = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for letter in range(length):
    if sentence[letter] in alphabet:
        new_sent += sentence[letter]
        count += 1
    else:
        if count != 0:
            print(new_sent, count)
        new_sent = ""
        count = 0
if count != 0:
    print(new_sent, count)