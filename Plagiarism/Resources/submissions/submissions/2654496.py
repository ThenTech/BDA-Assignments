def merge_lists(number):
    pass


def merge_sort(l):
    m = len(l)//2
    L = [ :m]
    R = [m+1: ]
    merge_sort(L)
    merge_sort(R)
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        list[k] = L[i]
        i += 1
        k+= 1
    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1