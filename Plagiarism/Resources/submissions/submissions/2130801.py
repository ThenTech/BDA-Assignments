x = int(input("x = "))
sum_1 = 0
sum_2 = 0

for value in range(1, x+1):
    for number in range(1,value+1):
        sum_2 = sum_2 + number
    sum_1 = sum_1 + sum_2
    sum_2 = 0

print(sum_1)