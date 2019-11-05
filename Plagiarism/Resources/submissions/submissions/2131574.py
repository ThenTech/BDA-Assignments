response = input("What is the n")
n = int(response)
sum1 = 0
sum2 = 0

for i in range(1, n+1):
    sum1 = sum1 + i
    sum2 = sum2 + sum1
print(sum2)
