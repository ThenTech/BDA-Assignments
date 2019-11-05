fibbo = [0,1]



def fibonacci_values(i):
    for index in range(i-2): # -1 omdat er al 2 getallen in de lijst staan, range moet altijd min 1x lopen
        fibbo.append(fibbo[index]+fibbo[index+1])
    return fibbo