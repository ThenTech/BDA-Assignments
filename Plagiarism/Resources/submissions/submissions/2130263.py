Amount = int(input("Give the amount: "))
Square = Amount
for x in range(Amount-1):
    Square *= Amount
print(Square)