def combinations(m, prefix):
    global subset
    if len(prefix) == m+3:
        print(prefix)
    else:
        for base in subset:
            if base not in prefix:
                base += ' '
                combinations(m, prefix + base)


n = int(input('Subset {1-n}: '))
m = int(input('Max length: '))
subset = ''

for number in range(n, 0, -1):
    subset += str(number)

combinations(m, '')