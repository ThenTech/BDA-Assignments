# write your code here

input = input("input: ")

alfabet = "abcdefghijklmnopqrstuvwxyz"



for i in alfabet:
    value = 0
    y = 0
    while y + 1 <= len(input):
        if i == input[y]:
            value =+ 1
    print(i, ": ", value, sep="")
        
