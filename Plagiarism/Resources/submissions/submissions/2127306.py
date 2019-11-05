c1 = float(input("Hoeveel 1 eurocenten heb je:"))
c2 = float(input("Hoeveel 2 eurocenten heb je:"))
c5 = float(input("Hoeveel 5 eurocenten heb je:"))
c10 = float(input("Hoeveel 10 eurocenten heb je:"))
c20 = float(input("Hoeveel 20 eurocenten heb je:"))

total = c1 * 1 + c2 * 2 + c5 * 5 + c10 * 10 + c20 * 20
total /= 100
total += 0.001

total_str = str(total)
new_str = total_str[0 : (len(total_str) - 1)]

print("You have " + new_str + " euro!", sep="")