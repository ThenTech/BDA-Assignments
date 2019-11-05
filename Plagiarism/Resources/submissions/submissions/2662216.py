def count_words(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    in_word = False

    for char in string:
        if char in alphabet and in_word == False:
            in_word = True
        
        if in_word == True and (char not in alphabet or char == string[len(string)-1]):
            count += 1
            in_word = False

    print(count)