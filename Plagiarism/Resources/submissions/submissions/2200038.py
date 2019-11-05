def count_words(string):
    a = "abcdefghijklmnopqrstuvwqyz"
    word = string.split()
    for letter in string:
        if letter in a:
            letter = len(word)
    print(letter)
            