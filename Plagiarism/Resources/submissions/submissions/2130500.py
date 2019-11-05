x = int(input())
fact = 0
sum_ = 1
for i in range(x):
    for q in range(i+1):
        sum_ *= q+1
    fact += sum_
    sum_ = 1
print(fact)
