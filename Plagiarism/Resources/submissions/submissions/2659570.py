nuc = ["A", "C", "G", "T"]
n = int(input("how many letters? "))


def nucleo(begin):
    global n
    global nuc
    if len(begin) == 0:
        begin = []
    or_begin = begin[:]
    for i in nuc:
        begin = or_begin[:]
        if len(begin)+1 == n:
            print("".join(begin)+i)
        else:
            begin += i
            nucleo(begin)


nucleo("")