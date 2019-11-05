def f_dna_helper(max, n, current):
    if (len(current) == n):
        for i in current:
            print(i, end=" ")
        print()
    else:
        for i in range(max):
            first = max - i
            new_current = current + [first]
            f_dna_helper(max - i - 1, n, new_current)

def f_dna(m, n):
    f_dna_helper(m, n, [])


f_dna(int(input()), int(input()))