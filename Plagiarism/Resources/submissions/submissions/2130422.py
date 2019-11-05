x = int(input())

sum_large = 0
for i in range(x):
    sum_small = 0
    for j in range(i+1):
        sum_small += j
    sum_large += sum_small
print(sum_large)