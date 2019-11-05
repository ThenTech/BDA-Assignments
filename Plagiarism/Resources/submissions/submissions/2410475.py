n = int(input())

def nucleobase(n):
    bases = ['A','C','G','T']
    
    result = []
    
    for b in bases:
        if n > 1:
            secondbases = nucleobase(n-1)
            for bs in secondbases:
                result.append(b + bs)
        else:
            result.append(b)
    
    return result
        

for x in nucleobase(n):
    print(x)