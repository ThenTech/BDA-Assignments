string = str(input("put your sentence here: "))

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

def remove_punctuation(s):
    string_remove = ""
    for letter in s:
        if letter not in punctuation:
            string_remove += letter
        else:
            print(" ")
    return string_remove

remove_punctuation(string)
string_split = remove_punctuation(string).split()

for word in string_split:
    print(word, len(word))