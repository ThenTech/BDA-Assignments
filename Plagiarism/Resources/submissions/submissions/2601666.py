coins1 = input("")
coins2 = input("")
coins5 = input("")
coins10 = input("")
coins20 = input("")
total_coins = int(int(coins1) + int(coins2) * 2 + int(coins5) * 5 + int(coins10) * 10 + int(coins20) * 20) / 100
print("You have", total_coins, "euro!")