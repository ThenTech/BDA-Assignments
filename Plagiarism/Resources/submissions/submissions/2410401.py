n = int(input())

def nucleobase(n):
    bases = ['A','C','G','T']
    
    result = []
    
    for b in bases:
        if n > 1:
            secondbases = nucleobases(n-1)
            for bs in secondbases:
                result.append(b + bs)
        else:
            result.append(b)
    
    return result
        

print(nucleobase(n))