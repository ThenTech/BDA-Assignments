amount = float(input("amount: "))
cents = (amount/100)+0.001
two = (cents // 2)
one = (cents - two*2)// 1
fifty = (cents -two*2 - one)//0.5
twen = (cents -two*2-one - fifty*0.5)//0.2
ten = (cents - two*2 - one - fifty * 0.5 - twen * 0.2)//0.1
five = (cents - two*2 - one - fifty * 0.5 - twen * 0.2 - ten * 0.1)//0.05
twoc = (cents - two*2 - one - fifty * 0.5 - twen * 0.2 - ten * 0.1 - five * 0.05)//0.02
onec = (cents - two*2 - one - fifty * 0.5 - twen * 0.2 - ten * 0.1 - five * 0.05 - twoc * 0.02)//0.01
print("2-euros: ", int(two))
print("1-euros: ",int(one))
print("50c-euros: ", int(fifty))
print("20c-euros: ", int(twen))
print("10c-euros: ", int(ten))
print("5c-euros: ", int(five))
print("2c-euros: ", int(twoc))
print("1c-euros: ", int(onec))