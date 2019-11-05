column = int(input("Columns: "))
row = int(input("Rows: "))
number = 1

for i in range(row):
    for j in range(column):
        print(str(number) + " ", end="")
        number += 1
    print()