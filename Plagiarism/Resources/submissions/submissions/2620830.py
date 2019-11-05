def replace(pattern, replacement, corpus):
    word=""
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_string = ""
    count = 0

    while count < len(corpus):
        if corpus[count] in abc or corpus[count] in ABC:
            word += corpus[count]
            if word == pattern:
                new_string += replacement
                word = ""
            count += 1
        else:
            new_string += word + corpus[count]
            count += 1
            word = ""
    if word != "":
        new_string += word
    return new_string