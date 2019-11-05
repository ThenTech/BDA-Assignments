sortedlist = []
def merge_lists(first,second):
    global sortedlist
    if len(first) == 0:
        sortedlist += second
        return sortedlist
    if len(second) == 0:
        sortedlist += first
        return sortedlist
    if int(first[0]) <= int(second[0]):
        sortedlist.append(first[0])
        return merge_lists(first[1:], second)
    else:
        sortedlist.append(second[0])
        return merge_lists(first, second[1:])
def merge_sort(l):
    global sortedlist
    if len(l) > 1:
        mid = (len(l)//2)
        list1 = merge_sort(l[:mid])
        list2 = merge_sort(l[mid:])
        sortedlist = []
        return merge_lists(list1, list2)
    else:
        return l