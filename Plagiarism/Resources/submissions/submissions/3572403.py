# write your code here
input = input()

half = len(input)/2
    
for i in range(half):
    buf = input[i]
    input[i] = input[len(input)-i]
    input[len(input)-i] = buf
print(input)