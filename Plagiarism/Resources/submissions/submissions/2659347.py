def collection(list, length, subset):
    #print(list, subset)

    if len(subset) == length + 3:
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


n = int(input("{1, ... , n} | n: "))
m = int(input("length: "))
list = []

for i in range(n, 0, -1):
    list.append(str(i))
collection(list, m, "")