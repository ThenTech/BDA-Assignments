alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sentence = input("Write a sentence: ")
index = 0

for char in sentence:
    if char not in alphabet:
        sentence = sentence[:index] + " " + sentence[index+1:]
    index += 1
    
list_words = sentence.split()

for word in list_words:
    print(word, len(word))