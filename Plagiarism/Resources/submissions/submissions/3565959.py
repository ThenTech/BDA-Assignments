n = int(input("Give value, greater than 0: "))
while n < 1:
    n = int(input("Give value, greater than 0: "))

bases = ["A", "C", "G", "T"]

for i in range(len(bases)):
    for j in range(len(bases)):
        print(bases[i], bases[j])
