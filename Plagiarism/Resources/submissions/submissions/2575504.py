import string

def count_words(string2):
    count = 0
    for i in range(len(string2)):
        if i == 0:
            if 65 <= ord(string2[0]) <= 90 or 97 <= ord(string2[0]) <= 122:
                count += 1
        else:
            if (65 <= ord(string2[i - 1]) <= 90 or 97 <= ord(string2[i - 1]) <= 122) and (65 <= ord(string2[i]) <= 90 or 97 <= ord(string2[i]) <= 122):
                continue
            else:
                if 65 <= ord(string2[i]) <= 90 or 97 <= ord(string2[i]) <= 122:
                    count += 1
    return count
