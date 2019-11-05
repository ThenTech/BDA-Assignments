def subset_helper(l, result):
    if len(l) == 0:
        # print(result)
        output = ""
        for i in result:
            output += str(i) + " "
        if len(output) != 0:
            output = output[:len(output) - 1]
        print(output)
    else:
        eerste = l[0]
        rest = l[1:]
        # don't add
        subset_helper(rest, result)
        # add
        subset_helper(rest, result + [eerste])


def subset(l):
    subset_helper(l, [])


subset(input().split())
