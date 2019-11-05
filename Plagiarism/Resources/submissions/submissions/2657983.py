number = input()
number = number.split()


def subset(n, word=""):
    word += n[0]+ " "
    if len(n) > 1:
        subset(n[1:], word[0: len(word)-2])
        subset(n[1:], word)
    print(word[:len(word)-1])
    

subset(number)
print()