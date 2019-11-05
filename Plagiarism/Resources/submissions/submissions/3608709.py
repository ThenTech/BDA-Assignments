coloms = int(input("Give the number of coloms you want:"))
rows = int(input("Give the number of rows you want:"))
for i in range(1,rows + 1):
    for j in range(1, coloms + 1):
        print(i * j, end=' ')
    print("\n")