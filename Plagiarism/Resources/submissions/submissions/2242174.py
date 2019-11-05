def count_words(string):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,"
    count = 1
    for i in range(len(string)):
        if string[i] not in alfabet:
            count += 1
    return count