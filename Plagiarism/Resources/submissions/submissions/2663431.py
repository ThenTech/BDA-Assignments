def collection(list, length, subset):
    if len(subset) == 2*length:
        print(subset[:-1])
    elif len(list) != 0:
        last = str(list[-1])
        rest = list[:-1]
        # add first
        collection(rest, length, subset + last + " ")
        # don't add first
        collection(rest, length, subset)


n = int(input("{1, ... , n} | n: "))
m = int(input("length: "))
list = [i for i in range(1, n+1)]

collection(list, m, "")