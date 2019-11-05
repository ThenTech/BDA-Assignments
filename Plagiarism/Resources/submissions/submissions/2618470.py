def count_words(string):
    count = 0
    for i in range(len(string)):
        if i == 0 and 97 <= ord(string[i]) <= 122:
            count += 1
        elif 97 <= ord(string[i]) <= 122:
            if 97 <= ord(string[i-1]) <= 122:
                continue
            else:
                count += 1
    return count