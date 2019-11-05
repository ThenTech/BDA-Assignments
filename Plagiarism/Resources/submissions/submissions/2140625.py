j = 0
k = 0
number = input("insert number here: ")
for i in range(len(number)):
    k = int(number[i])
    if k % 2 == 0:
        j = j + 1
        continue
    else:
        j = j + 0
print(j)# write your code here