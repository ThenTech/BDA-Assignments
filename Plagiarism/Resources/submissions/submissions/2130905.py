coins = int(input("Coins = ?\n"))

tosubstr = int((coins - (coins % 200))/200)
print("2-euros: " + str(tosubstr))
coins -= tosubstr*200

tosubstr = int((coins - (coins % 100))/100)
print("1-euros: " + str(tosubstr))
coins -= tosubstr*100

tosubstr = int((coins - (coins % 50))/50)
print("50c-euros: " + str(tosubstr))
coins -= tosubstr*50

tosubstr = int((coins - (coins % 20))/20)
print("20c-euros: " + str(tosubstr))
coins -= tosubstr*20

tosubstr = int((coins - (coins % 10))/10)
print("10c-euros: " + str(tosubstr))
coins -= tosubstr*10

tosubstr = int((coins - (coins % 5))/5)
print("5c-euros: " + str(tosubstr))
coins -= tosubstr*5

tosubstr = int((coins - (coins % 2))/2)
print("2c-euros: " + str(tosubstr))
coins -= tosubstr*2

tosubstr = int((coins - (coins % 1))/1)
print("1c-euros: " + str(tosubstr))
coins -= tosubstr*1
