def printHelper(length, bases, string):
    if len(string) == length:
        print(string)
    else:
        for i in bases:
            printHelper(length, bases, string + i)

def printDna(length):
    bases = 'ACGT'
    printHelper(length, bases, "")
    
printDna(int(input()))