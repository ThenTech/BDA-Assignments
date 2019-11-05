sentence = input("Give sentence: ")
new_sent = ""
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
for letter in range(len(sentence)):
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