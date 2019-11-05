punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ 0123456789"
total = 0

def count_words(string):
    global total
    for i in range(0, len(string) - 1):
        letter = string[i]
        next_letter = string[i+1]
        if letter in punctuation:
            if next_letter in punctuation:
                total = total
            else:
                total = total + 1
        else:
            continue
    print(total + 1)