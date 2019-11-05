# a version that returns a list of results
def ss_helper(s, current):
    if len(s) == 0:
        return [current]
    else:
        head = s[0]
        tail = s[1:]
        includedsets = ss_helper(tail, current)
        excludedsets = ss_helper(tail, current + [head])
        return includedsets + excludedsets

def subsets(s):
    return ss_helper(s, [])

def set_printer(lijst):
    for i in range(len(lijst)):
        if len(lijst[i]) == m:
            for j in range(len(lijst[i])):
                if j == len(lijst[i]) - 1:
                    print(lijst[i][j], end="")
                else:
                    print(lijst[i][j], end=" ")
            print()

n = int(input("Lengte set"))
m = int(input("Maximaal aantal"))

main_set = [i for i in range(1, n + 1)]
powerset = subsets(main_set)

set_printer(powerset)