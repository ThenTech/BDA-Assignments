sentence = input()
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
word = False
word1 = ""
for i in sentence:
    h = ""
    for j in alphabet:
        in_alphabet = False
        if i == j:
            if not(word):
                word1 = ""
            h = j
            in_alphabet = True
            word = True
            break
        if i == " ":
            break
    if not(in_alphabet):
        print(word1, len(word1))
        word = False
        
    if word:
        word1 += h
print(word1, len(word1))