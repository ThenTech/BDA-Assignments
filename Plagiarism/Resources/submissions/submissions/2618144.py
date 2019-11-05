def subset(l):
    l = l.split(' ')
    ll = []
    for el in l:
        ll.append(el)
    subset_helper(ll, [])

def subset_helper(l, result):
    if len(l) == 0:
        for x in result:
            if x == result[-1]:
                print(x)
            else:
                print(x, end= " ")
    else:
        eerste = l[0]
        rest = l[1:]
        # niet toevoegen
        subset_helper(rest, result)
        #  toevoegen
        subset_helper(rest, result + [eerste])

subset(input())
