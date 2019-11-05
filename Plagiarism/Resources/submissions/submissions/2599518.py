x = int(input("x"))
pro = 1
sum = 0

for i in range(1, x+1):
    pro *= i
    sum += pro
print(sum)