coloms = int(input("Give the number of coloms you want:"))
rows = int(input("Give the number of rows you want:"))

for i in range(0,rows):
    for j in range(1, coloms + 1):
        print(i * j + coloms, end=' ')
    print()
