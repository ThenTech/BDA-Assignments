L = []
for i in range(5):
    L.append(int(input()))
L[0] = .01*L[1]
L[1] = .02*L[1]
L[2] = .05*L[2]
L[3] = .10*L[3]
L[4] = .20*L[4]

som = 0
for i in L:
    som += i
print("You have", som, "euro")