# write your code here
euro1 = int(input("1 cent?"))
euro2 = int(input("2 cents?"))
euro5 = int(input("5 cents?"))
euro10 = int(input("10 cents?"))
euro20 = int(input("20 cents?"))
total = float(0.010 * euro1 + 0.020 * euro2 + 0.050 * euro5 + 0.100 * euro10 + 0.200 * euro20)
print("You have", total, "euro!")