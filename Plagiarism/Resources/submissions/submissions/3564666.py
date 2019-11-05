one_cent = int(input("One cents: ")) * 1
two_cent = int(input("Two cents: ")) * 2
five_cent = int(input("Five cents: ")) * 5
ten_cent = int(input("Ten cents: ")) * 10
twenty_cent = int(input("Twenty cents: ")) * 20
total = one_cent + two_cent + five_cent + ten_cent + twenty_cent
euro = total // 100
tens = total // 10 % 10
hundreds = total % 10

print("You have ", euro, ".", tens, hundreds, " euro!", sep="")
