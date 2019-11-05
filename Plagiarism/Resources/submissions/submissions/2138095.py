sentence = input("type your sentence here: ")
letter = "abcdefghijklmnopqrstuvw"

if letter in sentence:
    x = sentence.count(letter)
    print(letter,": ", x, sep="")
else:
    print(letter,": ", 0)