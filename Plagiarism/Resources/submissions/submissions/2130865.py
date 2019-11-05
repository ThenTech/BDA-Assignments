x = int(input("X:"))
lijst = list()
som = 0
for i in range(1, x+1):
    som += i
    lijst.append(som)
print(sum(lijst))