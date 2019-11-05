# write your code here

def recur(elements, result):
    if len(result) == 2:
        print(result)
        return
    
    recur(elements, result + elements[0])
    recur(elements[1:], result)


recur("ACGT", "")
