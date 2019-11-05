alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

string = input("Enter a single line containing a string: ")


def remove_layout(sentence):
    output = ""
    for i in sentence:
        if i in alphabet:
            output += i
        else:
            output += " "
    return output


tolist = remove_layout(string).split()

for i in tolist:
    print(i, len(i))
