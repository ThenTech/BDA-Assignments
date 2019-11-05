# write your code here

n = int(input('input: '))


if n == 0:
    print()
    exit()

list = ['A', 'C', 'G', 'T']

if n == 1:
    for i in list:
        print(i)
    exit()

n -= 1



def calc(n):
    if n > 0:
        listlength = len(list)
        for i in range(len(list)):

            list.append(list[i] + 'A')
            list.append(list[i] + 'C')
            list.append(list[i] + 'G')
            list.append(list[i] + 'T')

        for i in range(listlength):
            del list[0]

        calc(n - 1)



    return

calc(n)

for i in list:
    print(i)


