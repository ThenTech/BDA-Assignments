
def fibonacci_values(i):
    fibbo = [0,1]
    for index in range(i-2):
        fibbo.append(fibbo[index]+fibbo[index+1])
    return fibbo