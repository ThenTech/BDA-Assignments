def subset_help(l, result):
    if len(l) == 0:
        print(result)
    else:
        first = l[0]
        rest = l[1:]
        # don't add
        subset_help(rest, result)
        # add
        subset_help(rest, result + [first])

def subsets(l):
    subset_help(l, [])
    
set = input()
subsets(set)