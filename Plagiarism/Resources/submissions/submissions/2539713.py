column = int(input())
row = int(input())

count = 1

for r in range(row):
    for c in range(column):
        print(count,end=" ")
        count += 1
        if c == column - 1:
            print()
        