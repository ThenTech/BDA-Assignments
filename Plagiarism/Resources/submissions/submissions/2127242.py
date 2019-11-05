a = input("Amount of 1 eurocent coins = ")
b = input("Amount of 2 eurocent coins = ")
c = input("Amount of 5 eurocent coins = ")
d = input("Amount of 10 eurocent coins = ")
e = input("Amount of 20 eurocent coins = ")

a = int(a)
b = int(b) * 2
c = int(c) * 5
d = int(d) * 10 
e = int(e) * 20

total = (a + b + c + d + e)
total = str(total)

if len(total) == 1:
    print("You have ", "0", ".", "0", total, " euro!", sep="")
    
if len(total) == 2:
    print("You have ", "0", ".", total[0], total[1], " euro!", sep="")

if len(total) == 3:
    print("You have ", total[0], ".", total[1], total[2], " euro!", sep="")
    
if len(total) == 4:
    print("You have ", total[0], total[1], ".", total[2], total[3], " euro!", sep="")
