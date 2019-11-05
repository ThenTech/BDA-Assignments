fibbo = [0,1]
def fibonacci_values(i):
    for index in range(i-2):
        fibbo.append(fibbo[index]+fibbo[index+1])
    return fibbo