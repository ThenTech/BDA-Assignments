def count_words(string):
    l = string.split()
    n = "0123456789"
    z = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


    for i in range(0, len(l)-1):
        word = l[i]
        
        if n not in word and not len(word) <= 1 and z not in word:
            count += 1
    print(count)



