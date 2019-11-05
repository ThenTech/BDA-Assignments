c1 = float(input("Hoeveel 1 eurocenten heb je:"))
c2 = float(input("Hoeveel 2 eurocenten heb je:"))
c5 = float(input("Hoeveel 5 eurocenten heb je:"))
c10 = float(input("Hoeveel 10 eurocenten heb je:"))
c20 = float(input("Hoeveel 20 eurocenten heb je:"))

total = c1 * 1 + c2 * 2 + c5 * 5 + c10 * 10 + c20 * 20

x = str(total)[0:len(str(total) - 1)] or 0
y = str(total)[len(str(total) - 2] or 0
z = str(total)[len(str(total) - 1] or 0

print("You have ", x, ".", y, z, " euro!", sep="")
