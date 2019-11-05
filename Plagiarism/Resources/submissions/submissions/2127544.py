money = int(input("Give me the amount of money you paid: "))
euros2 = money // 200
euros1 = ((money)-(200*euros2)) // 100
euros50c = ((money)-(200*euros2)-(100*euros1)) // 50
euros20 = ((money)-(200*euros2)-(100*euros1)-(50*euros50c)) // 20
euros10 = ((money)-(200*euros2)-(100*euros1)-(50*euros50c)-(20*euros20)) // 10
euros5c = ((money)-(200*euros2)-(100*euros1)-(50*euros50c)-(20*euros20)-(10*euros10)) // 5
euros2c = ((money)-(200*euros2)-(100*euros1)-(50*euros50c)-(20*euros20)-(10*euros10)-(5*euros5c)) // 2
euros1c = ((money)-(200*euros2)-(100*euros1)-(50*euros50c)-(20*euros20)-(10*euros10)-(5*euros5c)-(2*euros2c)) // 1
print("2-euros:", euros2)
print("1-euros:", euros1)
print("50c-euros:", euros50c)
print("20c-euros:", euros20)
print("10c-euros:", euros10)
print("5c-euros:", euros5c)
print("2c-euros:", euros2c)
print("1c-euros:", euros1c)
