def write_words_and_count(string):
    abc = "abcdefghijklmnopqrstuvwxyz"
    Habc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    word = ""
    count = 0

    for i in string:
        if i in abc or i in Habc:
            word += i
            count += 1
        elif word != "" and count != 0:
            print(word + " " + str(count))
            word = ""
            count = 0
    if word != "" and count != 0:
        print(word + " " + str(count))

