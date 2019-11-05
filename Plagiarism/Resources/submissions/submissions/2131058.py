x = int(input())
som = 0
for i in range(x+1):
    for j in range(i+1):
        som += j
print(som)