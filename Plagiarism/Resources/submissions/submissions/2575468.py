import string

def count_words(string2):
    #hello = False
    count = 0
    for i in range(len(string2)):
        if i == 0:
            if 65 <= ord(string2[0]) <= 90 or 97 <= ord(string2[0]) <= 122:
                count += 1
                #hello = True
                #print("0")

        else:
            #if hello == False:
            #    if (65 <= ord(string2[i-1]) <= 90 or 97 <= ord(string2[i-1]) <= 122) and (65 <= ord(string2[i]) <= 90 or 97 <= ord(string2[i]) <= 122):
            #
            #        print("1")
            #        continue
            #print(string2[i-1], "i-1", string2[i], "i")
            if (65 <= ord(string2[i - 1]) <= 90 or 97 <= ord(string2[i - 1]) <= 122) and (65 <= ord(string2[i]) <= 90 or 97 <= ord(string2[i]) <= 122):
                #print("2")
                continue
            else:
                #print(string2[i])
                if 65 <= ord(string2[i]) <= 90 or 97 <= ord(string2[i]) <= 122:
                    count += 1
                    #print("3")
                #print("4")
                #if 65 <= ord(string2[0]) <= 90 or 97 <= ord(string2[0]) <= 122:
    return count
