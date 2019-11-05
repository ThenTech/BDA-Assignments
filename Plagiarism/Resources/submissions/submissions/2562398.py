def subset_help(l, result, m):
    if len(l) == 0:
        if len(result) == m:
            for i in result:
                print(i, end=" ")
            print()
    else:
        first = l[0]
        rest = l[1:]
        # don't add
        subset_help(rest, result, m)
        # add
        subset_help(rest, result + [first], m)

def subsets(l, m):
    subset_help(l, [], m)

def collections(n, m):
    list = [i for i in range(1, n+1)]
    subsets(list, m)

n = input()
m = input()
collections(n, m)