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

s = []
for element in input().split():
    s.append(int(element))
