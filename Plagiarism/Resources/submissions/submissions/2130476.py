Number = int(input("Give a number: "))
List = []
for x in range(Number):
    x += 1
    for y in range(1, x + 1):
        List += [y]
SumOfList = sum(List)
print(SumOfList)
