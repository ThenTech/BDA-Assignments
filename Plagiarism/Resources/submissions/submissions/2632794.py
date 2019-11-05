def subset(listy, current):
    if len(listy) == 0:
        for element in current:
            print(element, end=" ")
        print()
    else:
        head = listy[0]
        tail = listy[1:]
        excluded = current[:]
        included = current[:] + [head]
        subset(tail, included)
        subset(tail, excluded)

s = []
for element in input().split():
    s.append(int(element))

subset(s, [])