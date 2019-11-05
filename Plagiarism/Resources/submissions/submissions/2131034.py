x=int(input())
i=0
j=0
result=0
for i in range(1,x+1):
    for j in range(1,i+1):
        result +=j
print(result)