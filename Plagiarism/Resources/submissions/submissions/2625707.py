x = (input())
teller = 0
for i in x:
    if int(i) % 2 == 0:
        teller += 1
print(teller)