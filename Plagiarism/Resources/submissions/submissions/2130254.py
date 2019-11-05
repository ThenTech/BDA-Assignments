number = int(input("Number: "))
semi_sum = 0
sum = 0

for i in range(number+1):
    for j in range(i+1):
        if j != 0:
            semi_sum += j
    sum += semi_sum
    semi_sum = 0

print(sum)