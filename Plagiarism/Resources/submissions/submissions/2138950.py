# write your code here

input1 = input("input1")
input2 = input("input2")

alfabet = "abcdefghijklmnopqrstuvwxyz"

for i in alfabet:
    amount1 = 0
    amount2 = 0
    y = 0
    z = 0
    
    while y+1 <= len(input1):
        if i == input1[y]:
            amount1 += 1
        y += 1
    
    while z+1 <= len(input2):
        if i == input2[z]:
            amount2 += 1
        z += 1
        
    if amount1 != amount2:
        print(input1, "and", input2, "are not anagrams")
        break
    
if amount1 == amount2:
    print(input1, "and", input2, "are anagrams")