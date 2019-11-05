# user inputs
x = int(input("Give x a value (greater than 0):"))
y = int(input("Give y a value (greater than 0):"))

# default variable initialization
multi = 1

# starts calculation
for i in range(0, y):
    multi = multi * ((x - i) / (y - i))

# output converted to int because we don't want anything after the comma
print(int(multi))