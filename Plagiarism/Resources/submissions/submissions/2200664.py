import string
string2 = input("input: ")

def sentence_without_punctuation(string):
    sent_without_punct = ""
    punctuation = """?.!; :"'"""
    for letter in string:
        if letter not in punctuation:
            sent_without_punct += letter
            continue
        if letter == " ":
            sent_without_punct += " "
        if sent_without_punct == "":
            return ""
    return sent_without_punct

string2 = sentence_without_punctuation(string2)
lijst = string2.split()
for i in lijst:
    print(i, len(i), sep=" ")
