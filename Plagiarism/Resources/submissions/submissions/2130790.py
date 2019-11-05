total = int(input("Geef een prijs."))
euro2 = total//200
total = total - (euro2 * 200)
euro1 = total//100
total -= (euro1 * 100)
euro50c = total//50
total -= (euro50c*50)
euro20c = total//20
total -= (euro20c*20)
euro10c = total//10
total -= (euro10c*10)
euro5c = total//5
total -= (euro5c*5)
euro2c = total//2
total -= (euro2c*2)
euro1c = total//1
total -= (euro1c*1)
print("2-euros: ", euro2)
print("1-euros: ", euro1)
print("50c-euros: ", euro50c)
print("20c-euros: ", euro20c)
print("10c-euros: ", euro10c)
print("5c-euros: ", euro5c)
print("2c-euros: ", euro2c)
print("1c-euros: ", euro1c)