import string

sentence = input("Give a sentence: ")

new_string = ""
for char in sentence:
    if char not in string.punctuation and char not in """“”’“”""":
        new_string += char
    else:
        new_string += " "
sl = new_string.split(" ")
for i in sl:
    if i == "":
        continue
    test = True
    for j in i:
        if j not in string.ascii_letters:
            test = False
            break
    if test:
        print(i, len(i))
