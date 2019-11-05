def subset(l):
    subset_helper(l, [])


def subset_helper(l, result):
    if len(l) == 0:
        print(result)
    else:
        print(l)
        first = l[0]
        rest = l[1:]
        # add first
        subset_helper(rest, result)
        # don't add first
        subset_helper(rest, result + [first])


nums = input('Numbers (ex: 1 2 3): ')
l = nums.split(' ')
subset(l)