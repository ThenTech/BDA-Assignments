one = int(input("aantal 1 eurocenten?:"))
one2 = one * 1
two = int(input("aantal 2 eurocenten?:"))
two2 = two * 2
five = int(input("aantal 5 eurocenten?:"))
five2 = five * 5
ten = int(input("aantal 10 eurocenten?:"))
ten2 = ten * 10
twenty = int(input("aantal 20 eurocenten?:"))
twenty2 = twenty * 20
som = (one2 + two2 + five2 + ten2 + twenty2)
euros = som // 100
tiencenten = (som % 100) // 10
centen = (som % 10)

print("You have ", euros, ".", tiencenten, centen, " euro!", sep="")

