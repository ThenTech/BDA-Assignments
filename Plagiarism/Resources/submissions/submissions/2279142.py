def count_words(string):

    return len(string.split())


string= input("string: ")
for i in string:
    print(count_words(string))

