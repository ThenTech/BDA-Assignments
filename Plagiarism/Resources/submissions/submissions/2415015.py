DNA = 'ACGT'


def print_possibilities(n, base, prefix):
    global DNA
    if len(prefix+base) == n:
        print(prefix+base)
    elif len(prefix+base) > n:
        return
    else:
        for other_base in DNA:
            print_possibilities(n, other_base, prefix+base)


def get_base(n):
    global DNA
    for base in DNA:
        print_possibilities(n, base, "")


n = int(input('Count: '))
get_base(n)