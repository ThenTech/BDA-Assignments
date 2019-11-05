def subsets(li, total):
    if(len(li) == 0):
        print_total(total)
    else:
        head = li[0]
        tail = li[1:]
        with_head = subsets(tail, total + [head])
        without_head = subsets(tail, total)



def subsets_helper(li):
    subsets(li, [])

def print_total(li):
    for el in li:
        print(el, end=" ")
    print()

x = input()
s = []
for element in x.split():
    s.append(int(element))

subsets_helper(s)