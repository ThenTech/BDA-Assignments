# write your code here
digits=input("give a number")
total=0
for i in range (len(digits)):
    if int(digits[i])%2==0:
        total+=1
print(total)