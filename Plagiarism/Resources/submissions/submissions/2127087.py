total = int(input())
remaining = (total%200)
amountCoins = ((total-remaining)/200)
print("2-euros: " + str(int(amountCoins)))
total = remaining

remaining = (total%100)
amountCoins = ((total-remaining)/100)
print("1-euros: " + str(int(amountCoins)))
total = remaining

remaining = (total%50)
amountCoins = ((total-remaining)/50)
print("50c-euros: " + str(int(amountCoins)))
total = remaining

remaining = (total%20)
amountCoins = ((total-remaining)/20)
print("20c-euros: " + str(int(amountCoins)))
total = remaining

remaining = (total%10)
amountCoins = ((total-remaining)/10)
print("10c-euros: " + str(int(amountCoins)))
total = remaining

remaining = (total%5)
amountCoins = ((total-remaining)/5)
print("5c-euros: " + str(int(amountCoins)))
total = remaining

remaining = (total%2)
amountCoins = ((total-remaining)/2)
print("2c-euros: " + str(int(amountCoins)))
total = remaining

remaining = (total%1)
amountCoins = ((total-remaining)/1)
print("1c-euros: " + str(int(amountCoins)))
total = remaining