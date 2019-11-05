# write your code here

number = input("Numbers")
even = '02468'
counter = 0
for characters in number:
    if characters in even:
        counter += 1
print(counter)