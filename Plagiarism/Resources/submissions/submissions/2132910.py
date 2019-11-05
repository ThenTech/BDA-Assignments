# write your code here
# user inputs
x = int(input("Give x a value (greater than 0):"))
y = int(input("Give y a value (greater than 0):"))

# default variable initialization
multi = 1

# start calculation
for i in range(0, y - 1):
    multi = multi * ((x - i) / (y - i))

# deze lijn code miste. het laatste deel van de formule
multi = multi * (x - y + 1) / 1

# output converted to int because we don't want anything after the comma
print(int(multi))