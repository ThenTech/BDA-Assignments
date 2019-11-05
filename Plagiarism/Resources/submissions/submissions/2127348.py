c1 = int(input("Hoeveel 1 cents"))
c2 = int(input("Hoeveel 2 cents"))
c5 = int(input("Hoeveel 5 cents"))
c10 = int(input("Hoeveel 10 cents"))
c20 = int(input("Hoeveel 20 cents"))
total = ((c1 * 0.01) + (c2 * 0.02) + (c5 * 0.05) + (c10 * 0.10) + (c20 * 0.20)) / 100
if total < 1.00:
    print("You have ", total, "0 euro!", sep="")
else:
    print("You have ", total, " euro!", sep="")