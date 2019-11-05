# write your code here

number = input("Numbers")
even = '02468'
counter = 0
for characters in even:
    if even in number:
        counter += 1
print(counter)