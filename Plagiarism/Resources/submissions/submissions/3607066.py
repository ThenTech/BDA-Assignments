# write your code here

n = int(input())

def recur(elements, result, n):
    if len(result) == n:
        print(result)
        return
    
    recur(elements, result + elements[0])
    recur(elements[1:], result)


recur("ACGT", "", n)
