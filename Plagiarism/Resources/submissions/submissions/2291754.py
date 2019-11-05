def fibonacci_values(i):
    for index in range(i-2): # -2 omdat er al 2 getallen in de lijst staan, anders teveel getallen berekent
        fibbo.append(fibbo[index]+fibbo[index+1])
    print fibbo