x = input("Geef een waarde voor x in.")

sum1 = 0
sum2 = 0

for i in range(1, int(x)+1):
    for j in range(1, i+1):
        sum1 += j
    sum2 += sum1
    sum1 = 0
print(sum2)