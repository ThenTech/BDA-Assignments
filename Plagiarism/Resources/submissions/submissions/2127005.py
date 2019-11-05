total = input("")

twoEuro = int(total) // 200
rest = int(total) % 200
oneEuro = rest // 100
rest -= oneEuro * 100
fifty = rest // 50
rest -= fifty * 50
twenty = rest // 20
rest -= twenty * 20
ten = rest // 10
rest -= ten * 10
five = rest // 5
rest -= five * 5
two = rest // 2
rest -= two * 2
one = rest
print("2-euros: " + str(twoEuro )+ "\n1-euros: " + str(oneEuro )+ "\n50c-euros: " + str(fifty) + \
      "\n20c-euros: " + str(twenty) + "\n10c-euros: " + str(ten) + "\n5c-euros: " + str(five) + \
      "\n2c-euros: " + str(two) + "\n1c-euros: " + str(one))