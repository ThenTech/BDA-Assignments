alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sentence = input("Write a sentence: ")
new_sentence = ""

for char in sentence:
    if char in alphabet:
        new_sentence += char + " "

list_words = new_sentence.split()

for word in list_words:
    print(word, len(word))