list = []
n = int(input())
combinations = 4**n
bases = ['A', 'C', 'G', 'T']


def combine(n):
    sublist = []
    if n == 1:
        return bases
    else:
        for i in bases:
            for q in combine(n-1):
                sublist += [i+q]
    return sublist


for i in combine(n):
    print(i)
