a = int(input("type here the amount of coins of 1 eurocent: "))*1
b = int(input("type here the amount of coins of 2 eurocent: "))*2
c = int(input("type here the amount of coins of 5 eurocent: "))*5
d = int(input("type here the amount of coins of 10 eurocent: "))*10
e = int(input("type here the amount of coins of 20 eurocent: "))*20

total = a + b + c + d + e
total_euro = total/100

print("you have ", total_euro, "euro!")