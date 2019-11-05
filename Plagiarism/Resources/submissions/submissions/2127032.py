types = [200, 100, 50, 20, 10, 5, 2, 1]
text = ["2-euros:", "1-euros:", "50c-euros:", "20c-euros:", "10c-euros:", "5c-euros:", "2c-euros:", "1c-euros:"]
money = float(input("Please enter an amount of cents: "))
for x in range(len(types)):
    count = 0
    while money >= types[x]:
        money = money - types[x]
        count = count + 1
    print(text[x], count)