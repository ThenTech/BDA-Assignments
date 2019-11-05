string = ""

def count_words(string):
    string = str(string)
    string_split = string.split()
    return len(string_split)   

count_words(string)