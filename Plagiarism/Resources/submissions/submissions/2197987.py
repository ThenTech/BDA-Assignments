def count_words(string):
    l = string.split()
    n = "0123456789"


    for i in range(0, len(l)-1):
        word = l[i]
        count = 0
        if n not in word and not len(word) <= 1:
            count =+ 1
    print(count)


string = str(input("geef een string: "))
count_words(string)
