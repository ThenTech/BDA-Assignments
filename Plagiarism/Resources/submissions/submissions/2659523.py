def subset(list):
    subset_helper(list, "")


def subset_helper(list, result):
    if len(list) == 0 or list == ['']:
        print(result[:-1])
    else:
        first = list[0]
        rest = list[1:]
        # don't add first
        subset_helper(rest, result + first + " ")
        # add first
        subset_helper(rest, result)


numbers = input('Numbers (ex: 1 2 3): ')
list = numbers.split(' ')
subset(list)