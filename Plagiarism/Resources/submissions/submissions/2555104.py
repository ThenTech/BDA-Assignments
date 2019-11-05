inp = input().split()

def subset(lst):
    if len(lst) == 1:
        return ['', lst[0]]
    else:
        result = []
        subsub = subset(lst[1:])
        for item in subsub:
            result.append(item)
            result.append(lst[0] + ' ' + item)
        return result
    
for x in subset(inp):
    print(x)