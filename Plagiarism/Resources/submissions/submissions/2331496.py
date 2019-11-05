def is_unique(l):
    lengte = len(l)
    #zet alle waardes in een lijst
    for i in range(0, lengte):
        elements[i] = l[i]
    #vergelijkt de lijst met alle andere elementen in de lijst
    for i in elements:
        #teller mag 1 zijn want de lijst vergelijkt 1 keer met hetzelfde element
        teller = 0
        for j in elements:
            if i == j:
                teller += 1
        if teller >= 2:
            return False
        else:
            return True