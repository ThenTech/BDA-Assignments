list_int = int(input())
list = [i for i in range(list_int)]
n = int(input())
def subsets(list, n):
    list_len = len(list)
    subsets_recv(list,"",list_len,n)
def subsets_recv(lst,prefix,lst_len,n):
    if n == 0:
        print (prefix)
        return
    for i in range(lst_len):
        new_prefix = prefix+lst[i]
        subsets_recv(lst, new_prefix, list_len, n-1)
        
subsets(list, n)