# write your code here
counter = 0
x = input("Number:")


for i in x:
    if int(i) % 2 != 1:
        counter = counter + 1
print(counter)