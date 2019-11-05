import string
string2 = input("input: ")

def sentence_without_punctuation(string):
    return string

alphabet = "abcdefghijklmnopqrstuvwxyz"
string2 = sentence_without_punctuation(string2)
lijst = string2.split()
for i in lijst:
    print(i, len(i), sep=" ")
