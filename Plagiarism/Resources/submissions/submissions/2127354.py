c1 = int(input("Hoeveel 1 cents"))
c2 = int(input("Hoeveel 2 cents"))
c5 = int(input("Hoeveel 5 cents"))
c10 = int(input("Hoeveel 10 cents"))
c20 = int(input("Hoeveel 20 cents"))
total = ((c1 * 1) + (c2 * 2) + (c5 * 5) + (c10 * 10) + (c20 * 20)) / 100
if total < 1.00:
    print("You have ", total, "0 euro!", sep="")
else:
    print("You have ", total, " euro!", sep="")