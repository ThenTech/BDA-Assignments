length = int(input("length: "))
word = ""
bases = "ACGT"


def printer(length, bases, word):
    if len(word) == length:
        print(word)
    else:
        for ch in bases:
            printer(length, bases, word + ch)
            

printer(length, bases, word)