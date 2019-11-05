def combinations(m, prefix):
    global subset
    if len(prefix) == m:
        for i in range(len(prefix)):
            if i < len(prefix)-1:
                print(prefix[i] + ' ', end='')
            else:
                print(prefix[i])

    else:
        for base in subset:
            if len(prefix) > 0:
                if base not in prefix and int(base) < int(prefix[-1]):
                    combinations(m, prefix + base)
            else:
                combinations(m, prefix + base)

n = int(input('Subset {1-n}: '))
m = int(input('Max length: '))
subset = ''

for number in range(n, 0, -1):
    subset += str(number)

combinations(m, '')