def lucky_numbers(n):
    lijst = []
    for i in range(1,n+1):
        lijst += str(i)
    return function(lijst,n)
    
def function(lijst, n)
    i =1
    copy = []
    while True:
        if len(copy)!=0:
            lijst = copy[:]
            copy = []
        i += 1
        y = len(lijst)// i
        if y == 0:
            break
        else:
            for j in range(len(n)):
                if j%i!=0:
                    copy += lijst[j]
    return copy