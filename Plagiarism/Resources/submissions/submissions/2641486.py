n = int(input())
def print_combinations(list, n)
    list_len = len(list)
    rec_combinations(list, "", list_len, n)
def rec_combinations(lst, perfix, lst_len, n):
    if n == 0:
        print prefix
        return
    else:
        for i in range(lst_len):
            new_prefix = prefix+lst[i]
            rec_combinations(lst, new_prefix, lst_len, n-1)
            
p = ["A", "C", "G", "T"]
print_combinations(p, n)