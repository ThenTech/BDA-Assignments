def lucky_numbers(n):
    n = int(n)
    getallen = [x for x in range(1,n+1)]
    return filter(getallen, 2)

def filter(getallen, y):
    if y > len(getallen):
        return getallen
    else:
        new = []
        out = [x for x in range(y-1, len(getallen), y)]
        for x in range(len(getallen)):
            if x in out:
                continue
            new.append(getallen[x])
        lucky = filter(new, y+1)
        return lucky