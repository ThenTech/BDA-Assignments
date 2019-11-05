def sub_sets(list):
    return sub_sets_recur([], list)

def sub_sets_recur(current, subset):
    if len(subset) == 0:
        return [current]
    return sub_sets_recur(current, subset[1:])+
    sub_sets_recur(current+[subset[0]], subset[1:])
        
data = (input().split())
new_data = sub_sets(data)
for i in new_data:
    for j in i:
        print(j, end="")
    print()