InputColumns = int(input("Give the amount of columns: "))
InputRows = int(input("Give the amount of rows: "))
CurrentNumber = 1
for i in range(InputRows):
    for j in range(InputColumns):
        print(CurrentNumber, end=" ")
        CurrentNumber += 1
    print()
