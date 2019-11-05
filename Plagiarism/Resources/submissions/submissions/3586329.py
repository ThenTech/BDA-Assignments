columns = int(input())
rows = int(input())
count = 0

for i in range (rows):
    for j in range(columns):
        count += 1
        print(count, end=" ")
    print()