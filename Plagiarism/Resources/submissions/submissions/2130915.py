x = int(input())
tot = 0
for i in range(1, x+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    tot += factorial
print(str(tot))