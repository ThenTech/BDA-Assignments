def f_dna_helper(li, li2):
    if (len(li) == 0):
        for i in li2:
            print(i, end=" ")
        print()
    else:
        head = li[0]
        tail = li[1:]
        with_head = f_dna_helper(tail, li2 + [head])
        without_head = f_dna_helper(tail, li2)



def f_dna(str):
    li = str.split(' ')
    f_dna_helper(li, [])


f_dna(input())