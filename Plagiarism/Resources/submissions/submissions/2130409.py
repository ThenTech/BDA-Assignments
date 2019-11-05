x = int(input())
totresult

for q in range(x):
    result = 1
    for i in range(q+1):
        result *= i+1
        
    totresult += result
    
print(totresult)