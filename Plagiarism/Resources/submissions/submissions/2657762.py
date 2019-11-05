input = str(input(""))

som = 0
for i in input:
    if int(i) % 2 == 0:
        som += 1
print(som)