def count_words(string):
    counts = dict()
    a = input("Type in a sentence:")
    words = str.split(a)
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        return counts