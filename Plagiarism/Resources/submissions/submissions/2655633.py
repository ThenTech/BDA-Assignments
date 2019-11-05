def partition(lst, low, high):
    i = low-1
    pivot = lst[high]
    for j in range(low, high):
        if lst[j] <= pivot:
            i = i+1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], mst[i+1]
    return i+1

def quick_sort_recv(lst, low, high):
    if low < high:
        part = partition(lst, low, high)
        quick_sort_recv(lst, low, part-1)
        quick_sort_recv(lst, part+1, high)

def quick_sort(list):
    list_len = len(list) -1
    quick_sort_recv(list, 0, list_len)
    return list