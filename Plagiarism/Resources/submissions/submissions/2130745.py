x = int(input())
y = int(input())
lotx = 1
loty = 1
lotxy = 1

for amountx in range(x):
    lotx = lotx * (amountx + 1)
    
for amounty in range(y):
    loty = loty * (amounty + 1)
    
for amountxy in range(x - y):
    lotxy = lotxy * (amountxy + 1)
print(str(int(lotx/(loty * lotxy))))