def lucky_numbers(n):
    new_list = []
    [new_list.append(i) for i in range(1, n+1)]

    number = 2
    removed = True

    while removed:
        removed = False
        for x in new_list[:]:
            if x % number == 0:
                new_list.remove(x)
                removed = True
        number += 1

    return new_list