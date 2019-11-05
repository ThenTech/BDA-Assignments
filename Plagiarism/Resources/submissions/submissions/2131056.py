x = int(input())
som = 0
for i in range(x):
    for j in range(i):
        som += i
        
print(som)