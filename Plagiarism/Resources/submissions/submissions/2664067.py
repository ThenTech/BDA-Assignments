def shift(list, n):
    copy = []
    for i in range(len(list)):
        # i-th element, shifted n positions
        old_i = (i - n) % len(list)
        copy.append(list[old_i])
    return copy



list = [1, 2, 3, 4, 5]
print(shift(list, 0))
print(shift(list, 1))
print(shift(list, -2))
print(shift(list, 13))
print(shift(list, -13))
