def merge_lists(first, second):
    x = 0
    y = 0
    result = []
    while x < len(first) or y < len(second):
        if x == len(first):
            result += second[y:]
            break
        elif y == len(second):
            result += first[x:]
            break
        elif first[x] > second[y]:
            result.append(second[y])
            y += 1
        elif first[x] <= second[y]:
            result.append(first[x])
            x += 1
    return result
        


def merge_sort(l):
    if len(l) > 1:
        lista = merge_sort(l[:int(len(l)/2)])
        listb = merge_sort(l[int(len(l)/2):])
        return merge_lists(lista, listb)
    else return l