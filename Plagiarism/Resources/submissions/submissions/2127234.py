# write your code here
euro1 = int(input("1 cent?"))
euro2 = int(input("2 cents?"))
euro5 = int(input("5 cents?"))
euro10 = int(input("10 cents?"))
euro20 = int(input("20 cents?"))
total = 0.01 * euro1 + 0.02 * euro2 + 0.05 * euro5 + 0.10 * euro10 + 0.20 * euro20
print("You have ", total, "euro!")