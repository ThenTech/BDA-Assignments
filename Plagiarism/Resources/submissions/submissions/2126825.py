one = int(input("1 eurocent: "))
two = int(input("2 eurocent: "))
five = int(input("5 eurocent: "))
ten = int(input("10 eurocent: "))
twenty = int(input("20 eurocent: "))

total = 0
total += 0.01 * one
total += 0.02 * two
total += 0.05 * five
total += 0.10 * ten
total += 0.20 * twenty

print("\nYou have {0:.2f} euro!".format(total))