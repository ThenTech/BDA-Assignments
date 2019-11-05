def collection(list, length, subset):
    if len(subset) == 2*length:
        print(subset[:-1])
    else:
        if len(list) == 0:
            return
        first = list[0]
        rest = list[1:]
        # add first
        collection(rest, length, subset + first + " ")
        # don't add first
        collection(rest, length, subset)


list = []
n = int(input("{1, ... , n} | n: "))
m = int(input("length: "))

for i in range(n, 0, -1):
    list.append(str(i))
collection(list, m, "")