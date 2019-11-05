n = input()
length = len(n)


def sep(n):
    numberlist = []
    numsub = ''
    for i in n:
        if i == ' ':
            numberlist += [numsub]
            numsub =''
        else:
            numsub += i
    numberlist += [numsub]
    return numberlist


numberlist = sep(n)


def combine(numberlist, numbers):
    for i in range(numbers):
        for q in range(i+1, numbers):
            print(numberlist[i], numberlist[q])
        print(numberlist[i])


combine(numberlist, len(numberlist))
