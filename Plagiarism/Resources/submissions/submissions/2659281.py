def count_words(string):
    count = 0
    for i in range(len(string)):
        if i == 0 and 97 <= ord(string[i]) <= 122:
            count +=1
        else:
            if i <= len(string) -1:
                if (ord(string[i]) < 97 or ord(string[i]) > 122)  and 97 <= ord(string[i +1]) <= 122:
                    count +=1
    return count
                