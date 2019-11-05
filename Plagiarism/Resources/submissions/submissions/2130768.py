numberX = int(input())
numberY = int(input())

counter = 0
for i in range(0,numberY):
    for y in range(0,numberX):
        counter = counter + 1
        print(counter, end = " ")
    print()
