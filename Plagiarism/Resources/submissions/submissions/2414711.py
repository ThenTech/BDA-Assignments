l = input().split() + ['']

def sublist(list):
    result = []
    for l in list:
        if len(list)>1:
            for ls in sublist(list[1:]):
                result.append(l + ls)
        else:
            result.append(l)
            result.append('')
    return result
    
for x in sublist(l):
    print(x)