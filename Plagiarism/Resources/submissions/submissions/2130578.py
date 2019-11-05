rows = int(input("Amount of rows: "))
columns = int(input("Amount of columns: "))

if rows < 1 or columns < 1:
    print("Amount of rows and columns have to be more than 0")
else:
    product = columns * rows

    for row in range(rows):
        starting_value = row * columns +1
        ending_value = columns * (row + 1) + 1
        for number in range(starting_value, ending_value):
            print(number, end = " ")
        print()