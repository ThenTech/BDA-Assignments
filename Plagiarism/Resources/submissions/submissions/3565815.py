def lucky_numbers(n):
    new_list = [i for i in range(1, n+1)]

    number = 2
    removed = True

    while removed:
        removed = False
        index = 1
        for x in new_list[:]:
            if index % number == 0:
                new_list.remove(x)
                removed = True
            index += 1

        number += 1

    return new_list
