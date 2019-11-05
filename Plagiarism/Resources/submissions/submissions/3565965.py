n = int(input("Give value, greater than 0: "))
while n < 1:
    n = int(input("Give value, greater than 0: "))

bases = ["A", "C", "G", "T"]

length = len(bases)

if n == 1:
    for i in bases:
        print(i)


if n == 2:
    for i in range(length):
        for j in range(length):
            print(bases[i], bases[j], sep="")

if n == 3:
    for i in range(length):
        for j in range(length):
            for k in range(length):
                print(bases[i], bases[j], bases[k], sep="")

if n == 4:
    for i in range(length):
        for j in range(length):
            for k in range(length):
                for l in range(length):
                    print(bases[i], bases[j], bases[k], bases[l], sep="")

if n == 5:
    for i in range(length):
        for j in range(length):
            for k in range(length):
                for l in range(length):
                    for m in range(length):
                        print(bases[i], bases[j], bases[k], bases[l], bases[m], sep="")
